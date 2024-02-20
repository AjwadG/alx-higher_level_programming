#!/usr/bin/node

const args = process.argv;
const request = require('request');

request.get(args[2]).on('response', (res) => {
  console.log('code: ' + res.statusCode);
});
