#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

try {
  fs.writeFileSync(args[2], args[3], 'utf8');
} catch (err) {
  console.log(err);
}
