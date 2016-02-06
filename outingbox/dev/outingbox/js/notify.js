// browserify-shim entry has been added for the following plugin to not require nom jQuery, rather rely on script tag entry for jQuery
require('sweetalert');

module.exports.notify = function (msg) {
    swal({
        title: "Error!",
        text: msg,
        type: "error",
        timer: 2000,
        confirmButtonText: "Cool"
    });
};
