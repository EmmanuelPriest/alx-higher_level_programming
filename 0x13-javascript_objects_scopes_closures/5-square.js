#!/usr/bin/node

/* Defines Square class that inherits class Rectangle */
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Rectangle;
