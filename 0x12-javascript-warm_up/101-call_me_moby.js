#!/usr/bin/node
/* functions executes x time function */
exports.callMeMoby = function (x, theFunction) {
  for (let j = 0; j < x; j++) {
    theFunction();
  }
};
