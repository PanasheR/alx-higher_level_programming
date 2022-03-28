#!/usr/bin/node
//print starwars characters
const request = require('request');
const film = process.args[2];
const filmurl = `https://swapi-api.hbtn.io/api/films/${film}`;
request(filmurl, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (err, res, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
