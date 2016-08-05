$(document).ready(function() {

  //I.D. all the elements to be used
  var $last = $("#previous"); //previous button
  var $next = $("#next"); //next button
  var $full = $("#toggle-fullscreen"); //full screen toggle button
  var $car = $("#slider"); //the whole slider
  var $count = 1; //the current image
  var $total = 3; //the amount of images

  // hey, look, I know this isn't the best way to count the images
  //but for some reason, $("#images img").length isn't returning a value
  //trouble shooting that later on.

  $("#images img").hide(); //hide all images
  $("#" + $count).show(); //except the index image

  $last.click(function() {
    //when the 'last' button is clicked
    $("#" + $count).fadeOut(300, function() {
      //fade out the currently shown image

      //if the count is > 1
      if ($count > 1) {
        //decrement count
        $count--;
      } else {
        //else, loop back around so that the last image is shown
        $count = $total;
      }

      //find the next image
      $item = $("#" + $count);

      //fade in the next image
      $item.fadeIn(300);
    });
  })

  $next.click(function() {
    //when the 'next' button is clicked
    $("#" + $count).fadeOut(300, function() {
      //fade out the currently shown image

      //if the count is less than the total amount of image
      if ($count < $total) {
        //increment the count
        $count++;
      } else {
        //else, loop back around so that the first image is shown
        $count = 1;
      }

      //find the next image
      $item = $("#" + $count);

      //fade in the next image
      $item.fadeIn(300);
    });
  })

  $full.click(function() {
    //when the fullscreen toggle is clicked

    //if the slider is already full screen
    if ($car.hasClass('full')) {
      //remove the fullscreen class
      $car.removeClass('full');

      //change the button icon to the 'fullscreen' icon
      $full.html('<i class="material-icons">fullscreen</i>');
    } else {
      //else, add the fullscreen class
      $car.addClass('full');

      //change the button icon to the 'fullscreen exit' icon
      $full.html('<i class="material-icons">fullscreen_exit</i>');
    }
  })
})
