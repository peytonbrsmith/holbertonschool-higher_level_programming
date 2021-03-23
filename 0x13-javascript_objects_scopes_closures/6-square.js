#!/usr/bin/node
const OSquare = require('./5-square');
class Square extends OSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const y = this.width;
    let x = this.height;
    while (x > 0) {
      let row = '';
      for (let i = 0; i < y; i++) {
        row = row.concat(c);
      }
      console.log(row);
      x = x - 1;
    }
  }
}
module.exports = Square;
