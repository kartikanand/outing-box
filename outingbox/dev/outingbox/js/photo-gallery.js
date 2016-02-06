module.exports.photoGalleryInitData = {
    lazyLoad: 'ondemand',
    dots: true,
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    slidesToScroll: 3,
    centerPadding: '0px',
    prevArrow: $('.arrow-left'),
    nextArrow: $('.arrow-right'),
    responsive: [
        {
          breakpoint: 1199,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3
          }
        },
        {
          breakpoint: 991,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        }
    ]
};
