#!/usr/bin/node

const fs = require('fs');
const arg = process.argv;

fs.writeFile(arg[2], arg[3], 'utf-8', (err, data) => {
  if (err) { console.log(err); }
});
