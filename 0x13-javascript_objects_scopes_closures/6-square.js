#!/usr/bin/node

/* Defines Square class that inherits class Rectangle */
const FormerSquare = require('./5-square');
class Square extends FormerSquare {
  charPrint (c) {
    const squareVar = c === undefined ? 'X' : c;
    for (let n = 0; n < this.height; n++) {
      let rectVar = '';
      for (let m = 0; m < this.width; m++) {
        rectVar += squareVar;
      }
      console.log(rectVar);
    }
  }
}

module.exports = Square;
