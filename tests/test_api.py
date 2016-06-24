# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

import os
import pkg_resources

import httpretty
import mock
import pytest

from invenio_grobid.api import process_pdf_stream
from invenio_grobid.errors import GrobidRequestError


@pytest.fixture
def sample_pdf():
    """Provide pdf fixture."""
    return pkg_resources.resource_string(
        'tests', os.path.join('fixtures', 'article.pdf'))


@mock.patch('invenio_grobid.api.current_app')
def test_ok_response(current_app, httppretty_mock, sample_pdf):
    """A valid pdf results in a valid response from GROBID."""
    current_app.config = {
        'GROBID_HOST': 'http://localhost:8080'
    }
    url = os.path.join(current_app.config.get("GROBID_HOST"),
                       "processFulltextDocument")
    httpretty.register_uri(httpretty.POST, url, body='OK')

    assert process_pdf_stream(sample_pdf) == 'OK'


@mock.patch('invenio_grobid.api.current_app')
def test_ko_response(current_app, httppretty_mock, sample_pdf):
    """A 500 response from GROBID yields a GrobidRequestError."""
    current_app.config = {
        'GROBID_HOST': 'http://localhost:8080'
    }
    url = os.path.join(current_app.config.get("GROBID_HOST"),
                       "processFulltextDocument")
    httpretty.register_uri(httpretty.POST, url, status=500)

    with pytest.raises(GrobidRequestError):
        process_pdf_stream(sample_pdf)
