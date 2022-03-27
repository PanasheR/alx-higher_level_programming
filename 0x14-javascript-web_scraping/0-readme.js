#!/usr/bin/node
const fis = require('fs');
const arg = process.argv[2];
fis.readFile(arg, 'utf-8', (err, result) => {
  if (err) { console.log(err); } else { console.log(result); }
});
