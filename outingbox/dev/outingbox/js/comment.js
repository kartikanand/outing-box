var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

// Comment form submit handler
module.exports.commentFormHandler = function (ev) {
    ev.preventDefault();

    var commentsForm = $(this);
    var review = commentsForm.find('textarea').val();

    // Max review length : 512 characters
    if (review.length > 512) {
        notify("Too long");
        return false;
    }

    var url = commentsForm.attr('action');
    var data = commentsForm.serializeArray();

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        var newComment = $('<h5>'+data.username+' on '+data.date+'</h5>'+'<p>'+data.review+'</p>');
        $('.comment-wrapper').prepend(newComment);
    })
    .catch(function (err) {
        console.log(err);
    });
};
