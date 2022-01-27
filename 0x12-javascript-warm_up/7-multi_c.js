#!/usr/bin/node
const args = process.argv;
let count = 0;
if (isNaN(parseInt(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (count < parseInt(args[2])) {
    console.log('C is fun');
    count++;
  }
}
