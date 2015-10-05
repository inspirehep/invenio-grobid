/*
 * This file is part of Invenio.
 * Copyright (C) 2015 CERN.
 *
 * Invenio is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio. If not, see <http://www.gnu.org/licenses/>.
 *
 * In applying this licence, CERN does not waive the privileges and immunities
 * granted to it by virtue of its status as an Intergovernmental Organization
 * or submit itself to any jurisdiction.
 */

define([
  'jquery',
  'hgn!js/grobid/templates/error',
  'hgn!js/grobid/templates/result',
  'hgn!js/grobid/templates/success',
  'hgn!js/grobid/templates/waiting',
], function ($, errorTemplate, resultTemplate, successTemplate, waitingTemplate) {
  return {
    'GROBID': function (opts) {
      var payload,
          options = {};

      this.initGROBID = function (opts) {
        options['error_title'] = opts['error_title'] ||
          'GROBID has encountered an error.';
        options['error_explanation'] = opts['error_explanation'] ||
          'Please try again with the same PDF<br/>or inform the Invenio Developers.';
        options['uploadURL'] = opts['uploadURL'] || '/grobid/upload';
        options['submitURL'] = opts['submitURL'] || '/grobid/submit';

        this.handleFile();
        this.handleUpload();
        this.handleSubmit();
      };

      this.handleFile = function () {
        $('.grobid-file :file').on('change', function (e) {
          // See: http://davidwalsh.name/fakepath
          var fileName = $(this).val().replace('C:\\fakepath\\', '');

          $('.grobid-text').val(fileName);
        });
      };

      this.handleUpload = function () {
        $('.grobid-form').on('submit', function (e) {
          e.preventDefault();

          var formData = new FormData($('.grobid-form')[0]);

          $.ajax({
            type: 'POST',
            url: options['uploadURL'],
            data: formData,
            processData: false,
            contentType: false
          }).success(function (data) {
            payload = data;

            $('.container-results').html(resultTemplate(data));
          }).error(function (data) {
            $('.container-results').html(errorTemplate({
              error_title: options['error_title'],
              error_explanation: options['error_explanation'],
            }));
          });

          $('.container-results').html(waitingTemplate);
        });
      };

      this.handleSubmit = function () {
        $('.grobid-submit').on('click', function (e) {
          e.preventDefault();

          $.ajax({
            type: 'POST',
            url: options['submitURL'],
            data: JSON.stringify(payload),
            contentType: 'application/json'
          }).success(function (data) {
            payload = {};

            $('.container-results').html(successTemplate);
          }).error(function (data) {
            $('.container-results').html(errorTemplate({
              error_title: options['error_title'],
              error_explanation: options['error_explanation'],
            }));
          });

          $('.container-results').html(waitingTemplate);
        });
      };

      this.initGROBID(opts);
    },
  };
});
