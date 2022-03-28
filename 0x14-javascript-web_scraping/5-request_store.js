#!/usr/bin/node
// script gets file content and display

const fs = require('fs');
const request = require('request');
const arg = process.argv;
const URL = arg[2];

request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = body;
    fs.writeFile(arg[3], data, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
