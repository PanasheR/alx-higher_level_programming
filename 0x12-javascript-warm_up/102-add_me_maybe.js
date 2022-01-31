#!/usr/bin/node
// function increments then displays function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
