var q = require('q');

// Utility function that returns a promise to make a request to the server with passed arguments.
module.exports.makeRequestToServer = function (url, method, data, dataType) {
    if (!url) {
        q.reject(new Error());
    }

    return q(
        $.ajax({
            'url': url,
            'method': method,
            'dataType': dataType,
            'data': data
        })
    );
};
