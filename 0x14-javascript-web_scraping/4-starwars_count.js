#!/usr/bin/node
// script prints Wedge Antilles movies

const request = require('request');
const arg = process.argv;
const URL = arg[2];

request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const Data = JSON.parse(body);
    const results = Data.results;
    let sum = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) { sum += 1; }
      }
    }
    console.log(sum);
  }
});
