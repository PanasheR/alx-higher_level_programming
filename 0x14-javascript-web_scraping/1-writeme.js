#!/usr/bin/node
const fis = require('fs');
const arg = process.argv;
fis.writeFile(arg[2], arg[3], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
});
