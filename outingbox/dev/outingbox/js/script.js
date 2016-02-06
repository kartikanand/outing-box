var $ = require('jquery');

// browserify-shim entry has been added for the following plugins to not require npm jQuery, rather rely on script tag entry for jQuery
require('slick-carousel');
require('jquery-bar-rating');
require('selectize');

var getCurrentLocation = require('./location').getCurrentLocation;
var bookmarkEventHandler = require('./bookmark').bookmarkEventHandler;
var ratingInitData = require('./rating').ratingInitData;
var commentFormHandler = require('./comment').commentFormHandler;
var photoGalleryInitData = require('./photo-gallery').photoGalleryInitData;
var filterInitData = require('./filter').filterInitData;

// initialize all the things
$(function () {

    // Add event handler to bookmark span element if it exists
    // will only exist on activity and search page
    var bookmarkSpan = $('span.bookmark');
    if (bookmarkSpan.length > 0) {
        bookmarkSpan.click(bookmarkEventHandler);
    }

    // Initialize ratings
    // will only exist on activity and search page
    var ratingsClass = $('.rating');
    if (ratingsClass.length > 0) {
        ratingsClass.barrating(ratingInitData);
    }

    // Add form submit handler to comments form
    var commentsForm = $('#comments-form');
    if (commentsForm.length > 0) {
        commentsForm.submit(commentFormHandler);
    }

    // Initialize all the tooltips
    $('[data-toggle="tooltip"]').tooltip();

    var photoGallery = $(".photo-gallery");
    if (photoGallery.length > 0) {
        $('.photo-gallery').slick(photoGalleryInitData);
    }

    if ($('#category_auto_filter').length > 0) {
        $('#category_auto_filter').selectize(filterInitData);
    }

    if($('#location_auto_filter').length > 0) {
        $('#location_auto_filter').selectize(filterInitData);
    }

/*    getCurrentLocation()
    .then(function (data) {
    });*/

});
