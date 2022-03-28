$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (
    data, textStatus
  ) {
    $('#hello').append(data.hello);
  });
});
