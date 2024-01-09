#!/usr/bin/node
const dict = require('./101-data.js').dict;

const mydict = {};

for (const key in dict) {
  if (mydict[dict[key]] === undefined) {
    mydict[dict[key]] = [key];
  } else {
    mydict[dict[key]].push(key);
  }
}
console.log(mydict);
