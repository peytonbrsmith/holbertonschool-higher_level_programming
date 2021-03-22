#!/usr/bin/node

let x = 0;

process.argv.forEach((val, index) => {
  if (index === 2) {
    x = x + 1;
    console.log(`${val}`);
  }
});

if (x === 0) {
  console.log('No argument');
}
