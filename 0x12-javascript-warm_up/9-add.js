#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);
if (typeof num1 === 'number' && typeof num2 === 'number') {
  console.log(add(num1, num2));
} else {
  console.log('NaN');
}

function add (a, b) {
  return (a + b);
}
