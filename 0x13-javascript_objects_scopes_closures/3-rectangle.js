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
}

module.exports = Rectangle;
