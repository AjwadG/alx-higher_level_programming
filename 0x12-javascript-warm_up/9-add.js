#!/usr/bin/node

const arg = process.argv.slice(2, 4);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(arg[0], arg[1]);
