#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (let i = list.length - 1; i > -1; i--) {
    rev.push(list[i]);
  }
  return (rev);
};
