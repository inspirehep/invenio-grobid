..
    This file is part of Invenio.
    Copyright (C) 2015 CERN.

    Invenio is free software; you can redistribute it
    and/or modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation; either version 2 of the
    License, or (at your option) any later version.

    Invenio is distributed in the hope that it will be
    useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Invenio; if not, write to the
    Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
    MA 02111-1307, USA.

    In applying this license, CERN does not
    waive the privileges and immunities granted to it by virtue of its status
    as an Intergovernmental Organization or submit itself to any jurisdiction.

================
 Invenio Grobid
================

.. image:: https://img.shields.io/travis/inspirehep/invenio-grobid.svg
        :target: https://travis-ci.org/inspirehep/invenio-grobid

.. image:: https://img.shields.io/coveralls/inspirehep/invenio-grobid.svg
        :target: https://coveralls.io/r/inspirehep/invenio-grobid

.. image:: https://img.shields.io/github/tag/inspirehep/invenio-grobid.svg
        :target: https://github.com/inspirehep/invenio-grobid/releases

.. image:: https://img.shields.io/pypi/dm/invenio-grobid.svg
        :target: https://pypi.python.org/pypi/invenio-grobid

.. image:: https://img.shields.io/github/license/inspirehep/invenio-grobid.svg
        :target: https://github.com/inspirehep/invenio-grobid/blob/master/LICENSE


Invenio module to interact with Grobid API for metadata extraction from PDF.

* Free software: GPLv2 license
* Documentation: https://invenio-grobid.readthedocs.org.

*This is an experimental developer preview release.*

Features
========

This module provide an interface for uploading PDFs to a `Grobid`_ instance and allows to submit extracted metadata to a configurable callback.

NOTE: This packages assumes you have setup a local Grobid REST service. For more information about this and more, read the official Grobid documentation.

.. _Grobid: http://grobid.readthedocs.org/en/latest/


Installation
============

.. code-block:: shell

    pip install invenio-grobid


Note that you also need a running Grobid `REST service`_.

.. _REST service: http://grobid.readthedocs.org/en/latest/Grobid-service/


Configuration
=============

Add ``invenio_grobid`` package to your Invenio ``PACKAGES`` config in your
``overlay/config.py`` to be picked up by the Invenio application loader.


Configure the URL to your Grobid REST service with ``GROBID_HOST``.

.. code-block:: shell

    inveniomanage config set GROBID_HOST 'http://localhost:8080'


If you want to change your standard upload handler after extraction, update ``GROBID_RESULT_HANDLER``.

.. code-block:: shell

    inveniomanage config set GROBID_RESULT_HANDLER 'my_overlay.grobid:upload_handler'


Usage
=====

The uploader interface is available under the ``/grobid`` endpoint by default. E.g. http://localhost:4000/grobid

* Choose a PDF to extract metadata from and hit ``Upload``.
* Wait a bit and metadata will be displayed.
* Click on ``Submit`` button to push the metadata to your ``GROBID_RESULT_HANDLER``

*Special thanks to Joseph Boyd (@jcboyd) and Gilles Louppe (@glouppe) for Grobid support.*

Happy hacking and thanks for flying Invenio Grobid.

| INSPIRE Development Team
|   Email: feedback@inspirehep.net
|   Twitter: http://twitter.com/inspirehep
|   GitHub: https://github.com/inspirehep/invenio-grobid
|   URL: http://inspirehep.net
