#!/usr/bin/node
// script displays get status code

const request = require('request');
const arg = process.argv;

request(arg[2], function (error, response, body) {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode);
});
