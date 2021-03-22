#!/usr/bin/node
{
  let x = parseInt(process.argv[2]);
  if (isNaN(x)) {
    console.log('Missing size');
  } else {
    const y = x;
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
