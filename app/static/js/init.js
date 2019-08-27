$(document).ready(function(){
  $('.parallax').parallax();
  $('.sidenav').sidenav();
  if($(this).scrollTop() <= 0){
    $('nav').removeClass('add-shadow');
    $('.home-logo').removeClass('home-logo-below');
  }
  $(document).scroll(function() {
    if($(this).scrollTop() <= 0){
      $('.home-logo').removeClass('home-logo-below');
      $('nav').removeClass('add-shadow');
    }
    else{
      $('.home-logo').addClass('home-logo-below');
      $('nav').addClass('add-shadow');
    }
  });
  $('#refresh').click(function(){
    window.location.reload(true);
  });
});