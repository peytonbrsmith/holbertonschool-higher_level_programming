#!/usr/bin/node

const host = 'https://swapi-api.hbtn.io/api/films/?format=json';

$(function () {
  $.get(host, function (data, textStatus) {
    for (film of data.results) {
      $('#list_movies').append($('<li></li>').text(film.title));
    }
  });
});
