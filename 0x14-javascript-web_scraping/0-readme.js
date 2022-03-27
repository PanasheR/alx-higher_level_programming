#!/usr/bin/node
const fis = require('fs');
const arg = process.argv;
fis.readFile(arg[2], 'utf-8', (err, data) => {
  if (err) { console.log(err); } else {
    console.log(data);
  }
});
