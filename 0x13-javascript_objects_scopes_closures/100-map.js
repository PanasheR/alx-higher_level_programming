#!/usr/bin/node
// script that imports an array but file 100-data is absent
const set = require('./100-data').list;
console.log(set);
let count = 0;
const mapping = set.map(function (x) { return (x * count++); });
console.log(mapping);
