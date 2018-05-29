/*
 * KHAL | REMOVE | 2.0
 * Copyright (C) 2018  Rachael Melanson
 * Copyright (C) 2018  Henry Rodrick
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

$('#fileinput').on('change', function(e) {
    if($(e.target).val() === '') {
        console.log("Missing file")
        return;
    }

    $.ajax({
        url: '/upload',
        type: 'POST',
        data: new FormData($('form')[0]),
        cache: false,
        contentType: false,
        processData: false,
        xhr: function() {
            var xhr = $.ajaxSettings.xhr();
            if (xhr.upload) {
                xhr.upload.addEventListener('progress', function(e) {
                    xhr.upload.addEventListener('progress', function(e) {
                         if (e.lengthComputable) {
                             $('#upload-progress').attr({
                                 value: e.loaded,
                                 max: e.total
                             });
                         }
                     } , false);
                } , false);
            }
            return xhr;
        },
        success: function(data) {
			 $('#upload-progress').attr({
				 value: 100.0,
				 max: 100.0
			 });
            var jobId = data.jobId
            var url = "/job/" + jobId;
            function fetchStatus() {
                $.ajax({
                    url: url,
                    type: 'GET',
                    success: function(data) {
                        var progress = 0.0;
                        if (data.state === "PROCESSING") {
                            progress = data.progress;
							$('#processing-info').html(data.info);
                        } else if (data.state === "SUCCESS") {
                            progress = 100.0;
                        }
                        $('#processing-progress').attr({
                            value: progress,
                            max: 100.0
                        });

                        if (data.state === "SUCCESS") {
                            var url = "/result/" + jobId;
							$.get(url, function(filename) {
                                window.location.href = "download/" + filename;
								$('#processing-info').html('Finished');
							});
                        } else {
                            setTimeout(fetchStatus, 1000)
                        }
                    }
                })
            }
            fetchStatus()
        }
    });
});
