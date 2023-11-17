#!/usr/bin/node
// create a Square class

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
      return;
    }

    let shape = '';
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        shape += c;
      }
      if (h < this.height - 1) {
        shape += '\n';
      }
    }
    console.log(shape);
  }
}

module.exports = Square;
