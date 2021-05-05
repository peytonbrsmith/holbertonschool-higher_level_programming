#!/usr/bin/node

var request = require('request');

host = process.argv[2]

const options = {
    hostname: 'host',
    method: 'GET'
  }

request(host, function(err, res, body) {
  console.log(res.statusCode)
});
