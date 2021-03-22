#!/usr/bin/node

function fac (num) {
  if (isNaN(num)) { return 1; }
  if (num < 0) { return -1; } else if (num === 0) { return 1; } else { return (num * fac(num - 1)); }
}

const x = parseInt(process.argv[2]);

console.log(fac(x));
