// Carousel Main Banner

$(document).ready(function(){
    $('.main-banner-carousel').owlCarousel({
      items: 1, // Set the number of items to display
      loop: true, // Enable carousel loop
      autoplay: true, // Activate autoplay
      autoplayTimeout: 3000, // Sets the pause time between slides (in milliseconds)
      autoplayHoverPause: true // Pause autoplay when hovering over carousel
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
