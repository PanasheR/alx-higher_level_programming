#!/usr/bin/node
// script prints starwars title

const request = require('request');
const arg = process.argv;
const URL = 'https://swapi-api.hbtn.io/api/films/' + arg[2];

request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
