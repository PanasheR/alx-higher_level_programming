#!/usr/bin/node
const fis = require('fs');
const requesting = require('request');
const arg = process.argv;
const URL = arg[2];
requesting.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = body;
    fis.writeFile(arg[3], data, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
