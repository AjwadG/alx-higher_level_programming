#!/usr/bin/node

const args = process.argv;
const request = require('request');
const fs = require('fs');

request(args[2], (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(args[3], body, { flag: 'w+', encoding: 'utf-8' }, (err) => {
    if (err) console.log(err);
  });
});
