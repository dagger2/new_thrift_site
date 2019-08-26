$(document).ready(function(){
  $('.parallax').parallax();
  $('.sidenav').sidenav();

  if($(this).scrollTop() <= 0){
    $('.home-logo').removeClass('home-logo-below');
  }

  $(document).scroll(function() {
    if($(this).scrollTop() <= 0){
      $('.home-logo').removeClass('home-logo-below');
    }
    else{
      $('.home-logo').addClass('home-logo-below');
    }
  });

  $('#refresh').click(function(){
    window.location.reload(true);
  });

});