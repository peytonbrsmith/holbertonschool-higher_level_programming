#!/usr/bin/node

let x = 0;

process.argv.forEach((val, index) => {
  if (index === 2) {
    x = 1;
  }
});

if (x === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
