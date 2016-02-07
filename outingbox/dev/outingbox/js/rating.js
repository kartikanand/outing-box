var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

var readOnlyData = {
    theme: 'fontawesome-stars',
    showSelectedRating: false,
    hoverState: false,
    readonly: true
};

var editRatingData = Object.create(readOnlyData);
editRatingData.readonly = false;
editRatingData.onSelect = function(value, text, event) {
    // Return if manually setting the rating
    if (typeof(event) == undefined) {
        return;
    }

    var self = $(event.target);

    var form = self.parents(".rating-form");
    var data = form.serializeArray();

    var old_rating = self.parent().prev().data('old-rating');
    console.log(old_rating);

    var url = form.attr('action');

    if (value) {
        data.push({
            'name': 'new_rating',
            'value': value
        });
    } else {
        data.push({
            'name': 'delete',
            'value': 1
        });
    }

    makeRequestToServer(url, 'POST', data, 'json')
    .then(function (data) {
        console.log(data);
    })
    .catch(function (err) {
        console.log(err);
    });
};

// for ratings
module.exports.getRatingInitData = function (isReadOnly) {
    if (isReadOnly) {
        return readOnlyData;
    } else {
        return editRatingData;
    }
};
