#!/usr/bin/node

const args = process.argv;
let count = 0;
while (args[count] !== undefined) {
  count++;
}
if (count < 3) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
