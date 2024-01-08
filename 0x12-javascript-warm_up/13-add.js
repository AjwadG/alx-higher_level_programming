#!/usr/bin/node

module.exports.add = (a, b) => {
  if (isNaN(a) || isNaN(b)) {
    return ('NaN');
  } else {
    return (parseInt(a) + parseInt(b));
  }
};
