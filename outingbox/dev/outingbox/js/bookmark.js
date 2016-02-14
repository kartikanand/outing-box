var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

// For supporting bookmarks
module.exports.bookmarkEventHandler = function (ev) {
    // save this for future functions
    var self = $(this);

    var form = self.parent();
    var url = form.attr('action');
    var data = form.serializeArray();

    var removeBookmark = 0;
    // place is already bookmarked, user wants to delete bookmark
    if (self.hasClass('fa-bookmark')) {
        removeBookmark = 1;
        data.push({'name': 'delete', 'value': '1'});
    }

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        if (data.status == '0') {
            self.toggleClass('fa-bookmark-o');
            self.toggleClass('fa-bookmark');

            if (removeBookmark) {
                self.attr('data-original-title', 'Bookmark');
            } else {
                self.attr('data-original-title', 'Remove Bookmark');
            }
        } else {
            throw new Error();
        }
    })
    .catch(function (err) {
        if (err.responseJSON.status == -1) {
            notify("Please login to bookmark!");
        } else {
            throw err;
        }
    })
    .catch(function (err) {
        notify("Oops! we messed up. Please try again later.");
    });
};
