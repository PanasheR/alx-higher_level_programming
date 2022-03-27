#!/usr/bin/node
const requesting = require('request');
const arg = process.argv;
const URL = arg[2];
const set = {};
requesting.get(URL, (err, res, body) => {
  if (err) { console.log(err); } else {
    const data = JSON.parse(body);
    let user = 'default';
    for (let j = 0; j < data.length; j++) {
      if (data[j].completed === true) {
        if (!(data[j].userId in set)) {
          user = data[j].userId;
          set[user] = 1;
        } else {
          user = data[j].userId;
          set[user] += 1;
        }
      }
    }
    console.log(set);
  }
});
