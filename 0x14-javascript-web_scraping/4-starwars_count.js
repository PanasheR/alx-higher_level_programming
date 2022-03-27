#!/usr/bin/node
const requesting = require('request');
const arg = process.argv;
const URL = arg[2];
requesting.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let sum = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) { sum += 1; }
      }
    }
    console.log(sum);
  }
});
