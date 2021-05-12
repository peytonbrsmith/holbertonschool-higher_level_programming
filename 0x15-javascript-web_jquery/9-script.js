#!/usr/bin/node

const host = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(function () {
  $.get(host, function (data, textStatus) {
    $('#hello').text(data.hello);
  });
});
