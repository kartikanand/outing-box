var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

// Comment form submit handler
module.exports.commentFormHandler = function (ev) {
    ev.preventDefault();

    var commentsForm = $(this);
    var review = commentsForm.find('textarea').val();

    if (!review.trim()) {
        notify("Empty review not allowed!");
        return false;        
    }

    // Max review length : 512 characters
    if (review.length > 512) {
        notify("Too long");
        return false;
    }

    var url = commentsForm.attr('action');
    var data = commentsForm.serializeArray();

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        if (data.status == 0) {
            notify("Thanks! Your comments have been submitted for review. They'll be added within 24 hours!", "success", "Thanks!")
        }
        else {
            throw new Error(data);
        }
    })
    .catch(function (err) {
        notify("Oops! we messed up. Please try again later.");
    });
};
