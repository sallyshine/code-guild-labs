$(document).ready(function() {
  $("#input").on("keypress", function(event) {
    if (event.which === 13) {
      var value = $('#input').val();
      var item = $('<li/>');
      item.text(value);
      var checkbox = $('<input type="checkbox">');
      item.append(checkbox);
      var remove = $('<button/>');
      remove.text('Remove');
      remove.on("click", function() {
        item.remove()
      });
      item.append(remove);
      $("#todos").append(item);
      $('#input').val("");
    }
  });
});
