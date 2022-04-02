#!/usr/bin/node
// script imports an array and computes new array

const lists = require('./100-data').list;
console.log(lists);
const array = lists.map((x, idx) => x * idx);
console.log(array);
