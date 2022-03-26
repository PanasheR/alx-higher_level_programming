#!/usr/bin/node
exports.esrever = function (list) {
  const set = [];
  for (let i = list.length - 1; i >= 0; i--) {
    set.push(list[i]);
  }
  return set;
};
