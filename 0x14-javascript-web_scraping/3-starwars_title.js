#!/usr/bin/node
const requesting = require('request');
const arg = process.argv;
const URL = 'https://swapi-api.hbtn.io/api/films/' + arg[2];
requesting.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
