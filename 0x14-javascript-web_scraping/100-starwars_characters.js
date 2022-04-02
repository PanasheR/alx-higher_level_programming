#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const argv = process.argv;
const URL = `https://swapi-api.hbtn.io/api/films/${argv[2]}/`;
request(URL, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  for (const role of JSON.parse(body).characters) {
    request(role, function (error, response, body) {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
