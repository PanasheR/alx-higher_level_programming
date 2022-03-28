#!/usr/bin/node
const request = require('request');
const arg = process.argv;
const URL = arg[2];
const object = {};
request.get(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    let user = 'default';
    const data = JSON.parse(body);
    for (let j = 0; j < data.length; j++) {
      if (data[j].completed === true) {
        if (!(data[j].userId in object)) {
          user = data[j].userId;
          object[user] = 1;
        } else {
          user = data[j].userId;
          object[user] += 1;
        }
      }
    }
    console.log(object);
  }
});
