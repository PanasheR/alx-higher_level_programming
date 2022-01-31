#!/usr/bin/node
const args = process.argv;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else {
  let i, j, string;
  for (i = 0; i < parseInt(args[2]); i++) {
    string = '';
    for (j = 0; j < parseInt(args[2]); j++) {
      string += 'X';
    }
    console.log(string);
  }
}
