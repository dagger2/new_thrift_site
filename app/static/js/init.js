$(document).ready(function(){
  $('.parallax').parallax();
  $('.sidenav').sidenav();


  // if( $(window).scrollTop() === 0){
  //   console.log('at the top');
  //   $('.center-logo').width(700); 
  //   $('.center-logo').height(700);
  // }

  $('#refresh').click(function(){
    console.log('rfreshed');
    window.location.reload(true);

  });

});