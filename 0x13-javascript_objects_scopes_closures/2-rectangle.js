#!/usr/bin/node

/* Defines a rectangle class that creates and empty object */

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
    if (w === 0 || h === 0) {
      const emptyObj = new Rectangle();
    }
  }
}

module.exports = Rectangle;
