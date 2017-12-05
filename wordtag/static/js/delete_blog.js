$(document).ready(function() {
  var $deleteBlog = $('.delete-blog');

  $deleteBlog.on('click', function() {
    if(!confirm('Are you sure you want to delete this blog?'))
      return

    var csrftoken = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
      url: $deleteBlog.parent().find('a').attr('href'),
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrftoken
      }
    })
    .done(function() {
      $deleteBlog.parent().remove();

      if ($("#blogs").children('div').length == 0) {
        $("#blogs").append(
          '<p>You have no blogs!</p>'
        )
      }
    })
    .fail(function(error) {
      console.log(error);
    });

    return false;
  });
});
