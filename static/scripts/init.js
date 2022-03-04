$(document).ready(function(){
  $("#btn-a2").fadeOut();
  $("#btn-b2").fadeOut();
  $('.tooltipped').tooltip();
  $('.sidenav').sidenav();
  $('.tabs').tabs();
  $('.collapsible').collapsible({ accordion: false });
  $('.materialboxed').materialbox({
    onOpenStart: function(e){
      e.src = e.attributes['data-enlarge-image'].nodeValue;
    }    
  });

  M.toast({html: '<- More details here!'})
});

function expandAllAcademics() {
  $("#btn-a2").fadeIn();  $("#btn-a1").fadeOut();
  var instance = M.Collapsible.getInstance($("#cert-academic > .collapsible"));
  for (var i = 1; i < instance.$el[0].children.length; i++) instance.open(i);
}

function collapseAllAcademics() {
  $("#btn-a1").fadeIn();  $("#btn-a2").fadeOut();
  var instance = M.Collapsible.getInstance($("#cert-academic > .collapsible"));
  for (var i = 1; i < instance.$el[0].children.length; i++) instance.close(i);
}

function expandAllSpecializations() {
  $("#btn-b2").fadeIn();  $("#btn-b1").fadeOut();
  var instance = M.Collapsible.getInstance($("#cert-specializations > .collapsible"));
  for (var i = 1; i < instance.$el[0].children.length; i++) instance.open(i);
}

function collapseAllSpecializations() {
  $("#btn-b1").fadeIn();  $("#btn-b2").fadeOut();
  var instance = M.Collapsible.getInstance($("#cert-specializations > .collapsible"));
  for (var i = 1; i < instance.$el[0].children.length; i++) instance.close(i);
}


