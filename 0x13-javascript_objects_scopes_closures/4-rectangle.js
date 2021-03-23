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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
}
module.exports = Rectangle;
