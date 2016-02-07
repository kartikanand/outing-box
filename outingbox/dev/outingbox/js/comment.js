var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

// Comment form submit handler
module.exports.commentFormHandler = function (ev) {
    ev.preventDefault();

    var commentsForm = $(this);
    var review = commentsForm.find('textarea').val();

    // Max review length : 512 characters
    if (review.length > 5) {
        notify("Too long");
        return false;
    }


    var url = commentsForm.attr('action');

    var data = commentsForm.serializeArray();

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        var newComment = '<p>'+review+'</p>';
      + $('.comment-wrapper').append(newComment);
    })
    .catch(function (err) {
        console.log(err);
    });
};
