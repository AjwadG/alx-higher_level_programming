#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

if (args.length === 5) {
  let text = fs.readFileSync(args[2], 'utf8');
  text += fs.readFileSync(args[3], 'utf8');
  fs.writeFileSync(args[4], text);
} else {
  console.log('Usage: fileName firstfile secondFile destFile');
}
