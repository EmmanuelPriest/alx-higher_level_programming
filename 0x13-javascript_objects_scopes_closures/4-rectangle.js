#!/usr/bin/node

/* 
 * Defines a rectangle class that creates instance methods rotate()
 * and double()
 */

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
    let temp = 0;
    temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
