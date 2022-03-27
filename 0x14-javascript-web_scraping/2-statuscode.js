#!/usr/bin/node
const requesting = require('request');
const arg = process.argv;
requesting(arg[2], function (error, response, body) {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode);
});
