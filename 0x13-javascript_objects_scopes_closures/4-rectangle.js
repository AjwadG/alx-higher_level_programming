#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(w) || isNaN(h) || w < 1 || h < 1) { return; }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
};
