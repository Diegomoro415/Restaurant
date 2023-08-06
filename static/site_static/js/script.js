// Carousel Main Banner

$(document).ready(function(){
    $('.main-banner-carousel').owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,
      autoplayHoverPause: true
    });
});

// Login/Logout messages close after 3 seconds

$(document).ready(function () {
    setTimeout(function () {
        let messages = $(".messages");
        if (messages.length > 0) {
            messages.fadeOut(500, function () {
                $(this).alert('close');
            });
        }
    }, 3000);
});


// Scroll categories Menu

function scrollToCategory(event, category) {
    event.preventDefault();

    if ($("#" + category).length) {
      // Get the offset (position) of the target section relative to the top of the page
      var targetOffset = $("#" + category).offset().top;

      // Animate the scroll to the target section position
      $("html, body").animate({ scrollTop: targetOffset }, 1000);
    }
  }