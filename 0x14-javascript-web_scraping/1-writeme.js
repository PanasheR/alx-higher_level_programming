#!/usr/bin/node
// Script displays get status

const arg = process.argv;
const request = require('request');
request(arg[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else console.log('code:', response && response.statusCode);
});
