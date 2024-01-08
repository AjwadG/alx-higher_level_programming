#!/usr/bin/node

const arg = process.argv[2];

if (isNaN(arg)) {
  console.log(1);
} else {
  console.log(fact(arg));
}
function fact (arg) {
  if (arg === 1) {
    return (1);
  }
  return (arg * fact(arg - 1));
}
