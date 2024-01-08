#!/usr/bin/node

const arg = process.argv[2];
console.log(parseInt(arg) === NaN);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg));
}
