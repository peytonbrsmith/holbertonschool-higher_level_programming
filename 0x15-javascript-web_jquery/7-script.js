#!/usr/bin/node

const host = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

$(function()
{
	$.get(host, function(data, textStatus)
	{
		$("#character").text(data.name)
	});
});