var $ = require('jquery');

// require bootstrap components; soft link provided in current folder
require('./bootstrap/button');
require('./bootstrap/collapse');
require('./bootstrap/dropdown');
require('./bootstrap/modal');
require('./bootstrap/tooltip');
require('./jquery.unveil.js');

// browserify-shim entry has been added for the following plugins to not require npm jQuery, rather rely on script tag entry for jQuery
require('slick-carousel');
require('jquery-bar-rating');
require('selectize');

//var getCurrentLocation = require('./location').getCurrentLocation;
var bookmarkEventHandler = require('./bookmark').bookmarkEventHandler;
var getRatingInitData = require('./rating').getRatingInitData;
var commentFormHandler = require('./comment').commentFormHandler;
var initCommentForm = require('./comment').initCommentForm;
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

    $(".unviel").unveil();

    // Initialize read-only ratings
    // will only exist on activity and search page
    var readOnlyRatingsClass = $('.readonly-rating');
    if (readOnlyRatingsClass.length > 0) {
        readOnlyRatingsClass.barrating(getRatingInitData(true));
    }

    var editRatingClass = $('.rating-form .rating');
    if (editRatingClass.length > 0) {
        editRatingClass.barrating(getRatingInitData(false));
    }

    // Add form submit handler to comments form
    var commentsForm = $('#comments-form');
    if (commentsForm.length > 0) {
        initCommentForm(commentsForm);
        commentsForm.submit(commentFormHandler);
    }

    // Initialize all the tooltips
    $('[data-toggle="tooltip"]').tooltip();

    var photoGallery = $(".photo-gallery");
    if (photoGallery.length > 0) {
        $('.photo-gallery').slick(photoGalleryInitData);
    }

    var categoryAutoFilter = $('#category_auto_filter');
    if (categoryAutoFilter.length > 0) {
        categoryAutoFilter.selectize(filterInitData);
    }

    var locationAutoFilter = $('#location_auto_filter');
    if(locationAutoFilter.length > 0) {
        locationAutoFilter.selectize(filterInitData);
    }
});
