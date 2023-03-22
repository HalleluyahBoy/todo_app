$(function() {
    $('#add-form').on('submit', function(event) {
      event.preventDefault();
      $.post('/add', {
        reminder: $('#reminder').val(),
        date_time: $('#date_time').val()
      }, function() {
        location.reload();
      });
    });
  });
  