#!/usr/bin/node

/* Defines Square class that inherits class Rectangle */
const Square = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (C === undefined) {
      super.print();
    }
  }
}

module.exports = Square;
