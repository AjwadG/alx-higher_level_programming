#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

try {
  console.log(fs.readFileSync(args[2], 'utf8'));
} catch (err) {
  console.log(err);
}
