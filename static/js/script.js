

$(document).ready(function(){
  $("input").addClass('form-control');
  $('.navi').stickUp();
  $(".content-markdown").each(function(){
    var content = $(this).text();
    var contentMarked = marked(content);
    $(this).html(contentMarked);
  });
});
