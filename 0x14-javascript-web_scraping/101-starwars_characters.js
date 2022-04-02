#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const argv = process.argv;
const url = `https://swapi-api.hbtn.io/api/films/${argv[2]}/`;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const role = JSON.parse(body).characters;
    print(role, 0);
  }
});

function print (array, j) {
  if (j >= array.length) {
    return;
  }
  request.get(array[j], function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
    }
    return print(array, j + 1);
  });
}
