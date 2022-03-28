#!/usr/bin/node
// script to read and print file contents

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (err, result) => {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
