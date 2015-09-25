# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Utilities for Invenio Grobid."""

from .tasks import upload

from lxml import etree


NS = {'tei': 'http://www.tei-c.org/ns/1.0'}


def submit_handler(results):
    """Submit results asynchronously using `invenio_grobid.tasks.upload`."""
    return upload.delay(results)


def tei_to_dict(tei):
    parser = etree.XMLParser(encoding='UTF-8', recover=True)
    root = etree.fromstring(tei.encode('utf-8'), parser)

    result = {}

    abstract = get_abstract(root)
    if abstract and len(abstract) == 1:
        result['abstract'] = abstract[0].text

    authors = get_authors(root)
    if authors:
        result['authors'] = map(element_to_author, authors)

    title = get_title(root)
    if title and len(title) == 1:
        result['title'] = title[0].text

    references = get_references(root)
    if references:
        result['references'] = map(element_to_reference, references)

    return result


def element_to_author(el):
    result = {}

    name = []

    first = el.xpath('.//tei:persName/tei:forename[@type="first"]',
                     namespaces=NS)
    if first and len(first) == 1:
        name.append(first[0].text)

    middle = el.xpath('.//tei:persName/tei:forename[@type="middle"]',
                      namespaces=NS)
    if middle and len(middle) == 1:
        name.append(middle[0].text + '.')

    surname = el.xpath('.//tei:persName/tei:surname', namespaces=NS)
    if surname and len(surname) == 1:
        name.append(surname[0].text)

    result['name'] = ' '.join(name)

    affiliations = []
    for aff in el.xpath('.//tei:affiliation', namespaces=NS):
        for institution in aff.xpath('.//tei:orgName[@type="institution"]',
                                     namespaces=NS):
            affiliations.append({
                'value': institution.text
            })

    result['affiliations'] = affiliations

    return result


def element_to_reference(el):
    result = {}

    title = el.xpath('.//tei:analytic/tei:title[@level="a" and @type="main"]',
                     namespaces=NS)
    if title and len(title) == 1:
        result['ref_title'] = title[0].text

    result['authors'] = [
        element_to_author(e) for e in el.xpath('.//tei:author', namespaces=NS)
    ]

    # FIXME(jacquerie): missing pubnote.

    return result


def get_abstract(root):
    return root.xpath('//tei:profileDesc/tei:abstract/tei:p', namespaces=NS)


def get_authors(root):
    return root.xpath('//tei:fileDesc//tei:author', namespaces=NS)


def get_references(root):
    return root.xpath('//tei:text//tei:listBibl/tei:biblStruct', namespaces=NS)


def get_title(root):
    return root.xpath('//tei:titleStmt/tei:title', namespaces=NS)
