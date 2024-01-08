#!/usr/bin/node

const args = process.argv.slice(2);
const max = [0, 0];

for (let i = 0; args[i] !== undefined; i++) {
  const n = parseInt(args[i]);
  for (let j = 0; max[j] !== undefined; j++) {
    if (n >= max[j]) {
      if (j === 0) {
        max[1] = max[0];
        max[0] = n;
      } else {
        max[j] = n;
      }
      break;
    }
  }
}
console.log(max[1]);
