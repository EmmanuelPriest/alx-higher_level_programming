#!/usr/bin/node

/* Defines a rectangle class that creates an instance method print() */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      let rectVar = '';
      for (let m = 0; m < this.width; m++) {
        rectVar += 'X';
      }
      console.log(rectVar);
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    let wid = this.width * 2;
    let ht = this.height * 2;
  }
}

module.exports = Rectangle;
