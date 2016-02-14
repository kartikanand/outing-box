// browserify-shim entry has been added for the following plugin to not require nom jQuery, rather rely on script tag entry for jQuery
require('sweetalert');

module.exports.notify = function (msg, type, title) {
    type = type || "error";
    title = title || "Error!"
    swal({
        title: title,
        text: msg,
        type: type,
        timer: 3000,
        confirmButtonText: "Ok"
    });
};
