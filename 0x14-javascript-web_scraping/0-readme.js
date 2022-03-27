#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2];
fs.readFile(arg, 'utf-8', (err, result) => {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
