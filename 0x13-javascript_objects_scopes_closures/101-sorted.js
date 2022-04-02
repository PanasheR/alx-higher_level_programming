#!/usr/bin/node
// script imports a dictionary of occurrences
const dict = require('./101-data').dict;

const objects = {};
for (const [key, val] of Object.entries(dict)) {
  if (!(val in objects)) {
    objects[val] = [key];
  } else {
    objects[val].push(key);
  }
}
console.log(objects);
