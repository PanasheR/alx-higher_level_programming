#!/usr/bin/node
const args = process.argv;
const num1 = parseInt(args[2]);
console.log(factorial(num1));
function factorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
