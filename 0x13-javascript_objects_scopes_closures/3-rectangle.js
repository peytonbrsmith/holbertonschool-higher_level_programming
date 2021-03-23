#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const y = this.width;
    let x = this.height;
    while (x > 0) {
      let row = '';
      for (let i = 0; i < y; i++) {
        row = row.concat('X');
      }
      console.log(row);
      x = x - 1;
    }
  }
}
module.exports = Rectangle;
