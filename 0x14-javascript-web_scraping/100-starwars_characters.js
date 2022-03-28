#!/usr/bin/node
// script prints starwars cast

const request = require('request');
const film = process.argv[2];
const filmurl = `https://swapi-api.hbtn.io/api/films/${film}`;
request(filmurl, (err, res, body) => {
  if (!err) {
    const cast = JSON.parse(body).cast;
    cast.forEach((cast) => {
      request(cast, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
