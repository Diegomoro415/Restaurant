// Carousel Main Banner

$(document).ready(function(){
  // Initialize the Owl Carousel for the main banner
  $('.main-banner-carousel').owlCarousel({
      items: 1,
      loop: true,
      autoplay: true,
      autoplayTimeout: 3000,
      autoplayHoverPause: true
  });
});

// Close Login/Logout messages after 3 seconds

$(document).ready(function () {
  setTimeout(function () {
      let messages = $(".messages");
      if (messages.length > 0) {
          // Fade out and close the messages after 3 seconds
          messages.fadeOut(500, function () {
              $(this).alert('close');
          });
      }
  }, 3000);
});

// Scroll to categories in Menu

function scrollToCategory(event, category) {
  event.preventDefault();

  if ($("#" + category).length) {
      // Get the offset (position) of the target section relative to the top of the page
      var targetOffset = $("#" + category).offset().top;

      // Animate the scroll to the target section position
      $("html, body").animate({ scrollTop: targetOffset }, 1000);
  }
}

// Date Picker

$(function() {
  // Initialize the Datepicker
  $("#date").datepicker({
      dateFormat: "dd/mm/yy", // Date Format
      minDate: 0, // Set the current date as the minimum date
      beforeShowDay: function(date) {
          // Array with the days of the week when the restaurant is closed (Monday = 1, Tuesday = 2, etc.)
          var excludedDays = [1, 2]; // For example, excluding Monday and Tuesday

          // Check if the day is present in the array of excluded days
          var day = date.getDay();
          return [excludedDays.indexOf(day) === -1];
      }
  });
});
