#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log('0');
} else {
  /* Create an array with sorted list(in ascending order) */
  const list = args.sort((a, b) => a - b);
  /* find length of array */
  const len = list.length;
  /* print the second from last element */
  console.log(list[len - 2]);
}
