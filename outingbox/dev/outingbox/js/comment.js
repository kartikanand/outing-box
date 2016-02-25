var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

var addDeleteButtonToForm = function (commentsForm) {
    var deleteButton = commentsForm.find('#review-delete');
    if (deleteButton.length == 0) {
        deleteButton = $('<button type="submit" name="submit" value="delete" class="btn btn-danger" id="review-delete">Delete</button>');

        commentsForm.find('#review-button-group').append(deleteButton);

        initCommentForm(commentsForm);
    }
};

module.exports.initCommentForm = initCommentForm = function (commentsForm) {
    commentsForm.find("button").each(function () {
        $(this).bind("click keypress", function () {
            commentsForm.data("buttonId", this.id);
        });
    });
};

// Comment form submit handler
module.exports.commentFormHandler = function (ev) {
    ev.preventDefault();
    var commentsForm = $(this);
    var data = commentsForm.serializeArray();
    var url = commentsForm.attr('action');
    var delete_review = false;

    if (commentsForm.data("buttonId") == "review-delete") {
        delete_review = true;
        data.push({
            'name': 'delete',
            'value': 1
        });
    } else {
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
    }

    var user_review = $("#user-review");

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        if (data.status == 0) {
            if(delete_review) {
                notify('Review Deleted!', 'success', 'Cool');
                $("#edit-review-modal form textarea").val('');
                $("#review-button").text('Add a review!');

                if (user_review.length > 0) {
                    user_review.remove();
                }
            } else {
                $("#edit-review-modal form textarea").val(review);
                $("#review-button").text('Edit my review!');
                notify("Thanks for the review!", "success", "Thanks!");

                var commentHeaderText = data.username+" on "+data.date;
                var commentHeader = $("<h5 class='text-muted'></h5>");
                commentHeader.text(commentHeaderText);
                
                var commentBodyText = review;
                var commentBody = $("<p></p>");
                commentBody.text(commentBodyText);

                if (user_review.length > 0) {
                    user_review.empty();
                } else {
                    user_review = $("<div id='user-review'></div>");
                    $('#comments-wrapper').append(user_review);
                }
                
                user_review.append(commentHeader);
                user_review.append(commentBody);

                var firstReviewHeader = $("#comments-wrapper h3");
                if(firstReviewHeader.length > 0) {
                    firstReviewHeader.remove();
                }

                addDeleteButtonToForm(commentsForm);
            }
        }
        else {
            throw new Error();
        }
    })
    .catch(function (err) {
        if (err.responseJSON.status == -1) {
            notify("Please login to add a review!");
        } else {
            notify("Oops! we messed up. Please try again later.");
        }
    })
    .finally(function () {
        $('#edit-review-modal').modal('hide');
    });
};
