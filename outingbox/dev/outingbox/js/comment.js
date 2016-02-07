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
        var newCommentHeader = $('<h5 class="text-muted"></h5>');

        // Set .text() to save from XSS
        newCommentHeader.text(data.username+' on '+data.date);
        
        var newComment = $('<p></p>');

        // Set .text() to save from XSS
        newComment.text(data.review);
        
        $('.comment-wrapper').prepend(newCommentHeader);
        newCommentHeader.after(newComment);
    })
    .catch(function (err) {
        console.log(err);
    });
};
