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

"""Mapping from Grobid's TEI to the internal dict representation."""

from lxml import etree
from six import text_type


NS = {'tei': 'http://www.tei-c.org/ns/1.0'}


def tei_to_dict(tei):
    parser = etree.XMLParser(encoding='UTF-8', recover=True)
    tei = tei if not isinstance(tei, text_type) else tei.encode('utf-8')
    root = etree.fromstring(tei, parser)

    result = {}

    abstract = get_abstract(root)
    if abstract and len(abstract) == 1:
        result['abstract'] = abstract[0].text

    authors = get_authors(root)
    if authors:
        result['authors'] = map(element_to_author, authors)

    keywords = get_keywords(root)
    if keywords and len(keywords) == 1:
        result['keywords'] = extract_keywords(keywords[0])

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


def extract_keywords(el):
    return [{'value': e.text} for e in el.xpath('.//tei:term', namespaces=NS)]


def element_to_reference(el):
    result = {}

    result['ref_title'] = extract_reference_title(el)

    result['authors'] = [
        element_to_author(e) for e in el.xpath('.//tei:author', namespaces=NS)
    ]

    result['journal_pubnote'] = extract_reference_pubnote(el)

    return result


def extract_reference_title(el):
    title = el.xpath(
        './/tei:analytic/tei:title[@level="a" and @type="main"]',
        namespaces=NS
    )
    if title and len(title) == 1:
        return title[0].text


def extract_reference_pubnote(el):
    result = {}

    journal_title = el.xpath('./tei:monogr/tei:title', namespaces=NS)
    if journal_title and len(journal_title) == 1:
        result['journal_title'] = journal_title[0].text

    journal_volume = el.xpath(
        './tei:monogr/tei:imprint/tei:biblScope[@unit="volume"]',
        namespaces=NS
    )
    if journal_volume and len(journal_volume) == 1:
        result['journal_volume'] = journal_volume[0].text

    journal_issue = el.xpath(
        './tei:monogr/tei:imprint/tei:biblScope[@unit="issue"]',
        namespaces=NS
    )
    if journal_issue and len(journal_issue) == 1:
        result['journal_issue'] = journal_issue[0].text

    year = el.xpath(
        './tei:monogr/tei:imprint/tei:date[@type="published"]/@when',
        namespaces=NS
    )
    if year and len(year) == 1:
        result['year'] = year[0]

    pages = []

    page_from = el.xpath(
        './tei:monogr/tei:imprint/tei:biblScope[@unit="page"]/@from',
        namespaces=NS
    )
    if page_from and len(page_from) == 1:
        pages.append(page_from[0])

    page_to = el.xpath(
        './tei:monogr/tei:imprint/tei:biblScope[@unit="page"]/@to',
        namespaces=NS
    )
    if page_to and len(page_to) == 1:
        pages.append(page_to[0])

    result['page_range'] = '-'.join(pages)

    return result


def get_abstract(root):
    return root.xpath('//tei:profileDesc/tei:abstract/tei:p', namespaces=NS)


def get_authors(root):
    return root.xpath('//tei:fileDesc//tei:author', namespaces=NS)


def get_keywords(root):
    return root.xpath('//tei:profileDesc/tei:textClass/tei:keywords',
                      namespaces=NS)


def get_references(root):
    return root.xpath('//tei:text//tei:listBibl/tei:biblStruct', namespaces=NS)


def get_title(root):
    return root.xpath('//tei:titleStmt/tei:title', namespaces=NS)
