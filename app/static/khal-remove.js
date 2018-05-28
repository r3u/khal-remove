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
            var jobId = data.jobId
            var url = "/job/" + jobId;
            function fetchStatus() {
                $.ajax({
                    url: url,
                    type: 'GET',
                    success: function(data) {
                        var progress = 0.0;
                        if (data.state === "PROCESSING") {
                            progress = data.progress
                        } else if (data.state === "SUCCESS") {
                            progress = 100.0;
                        }
                        $('#processing-progress').attr({
                            value: progress,
                            max: 100.0
                        });

                        if (data.state === "SUCCESS") {
                            var url = "/result/" + jobId;
                            $('#downloads-section').html(
                                '<a href="' + url + '">Click me!</a>'
                            );
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
