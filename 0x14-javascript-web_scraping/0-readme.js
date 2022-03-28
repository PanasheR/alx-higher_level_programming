#!/usr/bin/node
// script prints file content

const file = process.argv[2];
const fis = require('fs');

fis.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
