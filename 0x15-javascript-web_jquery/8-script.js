$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (
    data, textStatus
  ) {
    $(data.results).each(function (i, item) {
      $('#list_movies').append('<li>' + item.title + '</li>');
    });
  });
});
