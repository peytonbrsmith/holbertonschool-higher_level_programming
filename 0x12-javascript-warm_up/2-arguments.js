#!/usr/bin/node

let x = 0;

process.argv.forEach((val, index) => {
  if (index > 1) {
    x = x + 1;
  }
});

if (x === 1) {
  console.log('Argument found');
} else if (x > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
