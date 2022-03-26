#!/usr/bin/node
exports.logMe = function (item) {
  if (this.counter === undefined) { this.counter = 0; }
  console.log(this.counter + ': ' + item);
  this.counter += 1;
};
