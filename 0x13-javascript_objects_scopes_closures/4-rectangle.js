#!/usr/bin/node
// create a Rectangle class

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }

    this.width = w;
    this.height = h;
  }

  print () {
    let shape = '';
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        shape += 'X';
      }
      if (h < this.height - 1) {
        shape += '\n';
      }
    }
    console.log(shape);
  }

  rotate () {
    const tmpWidth = this.width;
    this.width = this.height;
    this.height = tmpWidth;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
