$(document).ready(function(){
  $('.tooltipped').tooltip();
  $('.sidenav').sidenav();
  $('.collapsible').collapsible();
  $('.materialboxed').materialbox({
    onOpenStart: function(e){
      e.src = e.attributes['data-enlarge-image'].nodeValue;
    }    
  });

  M.toast({html: '<- More details here!'})
});

/*
$('.materialboxed').materialbox('large': 'data-enlarge-image');
$('.boxwithlarge').materialbox({
  onOpenStart: function(e){
    e.src = e.attributes['data-enlarge-image'].nodeValue;
  }
})

*/


