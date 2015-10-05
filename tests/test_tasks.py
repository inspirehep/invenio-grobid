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

import pytest

from mock import patch

from invenio.celery import celery

from invenio_grobid.api import submit_record

from invenio.testsuite import InvenioTestCase


class TestTasks(InvenioTestCase):

    """Test invenio_grobid's Tasks."""

    def setup_class(self):
        """Load a valid fixture."""
        celery.conf['CELERY_ALWAYS_EAGER'] = True
        self.sample_record = {
            "title": "Test title",
            "authors": ["J. Lavik"],
        }
        self.sample_record_inserted = {
            "control_number": 1,
            "title": "Test title",
            "authors": ["J. Lavik"],
        }

    @patch('invenio_records.api.create_record')
    def test_submission(self, create_record):
        create_record.return_value = self.sample_record_inserted
        result = submit_record(self.sample_record)
        assert result.get() == self.sample_record_inserted
