#!/usr/bin/node
// script that concats 2 files
const argv = process.argv;
if (argv.length !== 5) {
  console.error('Incorrect num of arguments');
} else {
  const fs = require('fs');
  const target = argv[4];
  let str = '';
  str = str.concat(fs.readFileSync(argv[2]), fs.readFileSync(argv[3]));
  fs.writeFile(target, str, (err) => {
    if (err) console.log(err);
  });
}
