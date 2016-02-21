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

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        if (data.status == 0) {
            if(delete_review) {
                notify('Review Deleted!', 'success', 'Cool');
                $("#edit-review-modal form textarea").val('');
                $("#review-button").text('Add a review!');
                addDeleteButtonToForm(commentsForm);
            } else {
                $("#edit-review-modal form textarea").val(review);
                $("#review-button").text('Edit my review!');
                notify("Thanks! Your comments have been submitted for review. They'll be added within 24 hours!", "success", "Thanks!");
            }
        }
        else {
            console.log(data);
            throw new Error(data);
        }
    })
    .catch(function (err) {
        console.log(err);
        notify("Oops! we messed up. Please try again later.");
    })
    .finally(function () {
        $('#edit-review-modal').modal('hide');
    });
};
