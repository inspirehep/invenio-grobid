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

"""API functions to interact with Grobid REST API."""

import os

import requests

import six

from werkzeug.utils import import_string

from flask import current_app

from .errors import GrobidRequestError


def process_pdf_stream(pdf_file):
    """Process a PDF file stream with Grobid, returning TEI XML results."""
    response = requests.post(
        url=os.path.join(current_app.config.get("GROBID_HOST"),
                         "processFulltextDocument"),
        files={'input': pdf_file}
    )

    if response.status_code == 200:
        return response.text
    else:
        raise GrobidRequestError(response.reason)


def submit_record(results):
    """Submits the record in the way determined by `GROBID_RESULT_HANDLER`."""
    handler = current_app.config.get("GROBID_RESULT_HANDLER")
    if isinstance(handler, six.string_types):
        handler = import_string(handler)
    return handler(results)
