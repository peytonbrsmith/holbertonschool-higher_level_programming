#!/usr/bin/node
{
  let x = parseInt(process.argv[2]);

  if (isNaN(x)) {
    console.log('Missing number of occurences');
  } else {
    while (x > 0) {
      console.log('C is fun');
      x = x - 1;
    }
  }
}
