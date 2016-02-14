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
            var newCommentHeader = $('<h5 class="text-muted"></h5>');

            // Set .text() to save from XSS
            newCommentHeader.text(data.username+' on '+data.date);
            
            var newComment = $('<p></p>');

            // Set .text() to save from XSS
            newComment.text(data.review);
            
            $('.comment-wrapper').prepend(newCommentHeader);
            newCommentHeader.after(newComment);
        }
        else {
            throw new Error(data);
        }
    })
    .catch(function (err) {
        notify("Oops! we messed up. Please try again later.");
    });
};
