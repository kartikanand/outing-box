var makeRequestToServer = require('./utils').makeRequestToServer;
var notify = require('./notify').notify;

var getIsRatingReadOnly = function () {
    var canedit_input = $('input.can-edit');
    if (canedit_input.length > 0)
    {
        return false;
    }

    return true;
};

// for ratings
module.exports.ratingInitData = {
    theme: 'fontawesome-stars',
    showSelectedRating: false,
    hoverState: false,
    readonly: getIsRatingReadOnly(),
    onSelect:function(value, text, event) {
        // Return if manually setting the rating
        if (typeof(event) == undefined) {
            return;
        }

        console.log(this);

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
    },
    onClear:function(value, text) {
    }
};
