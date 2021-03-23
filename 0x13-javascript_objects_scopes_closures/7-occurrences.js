#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  list.forEach((val) => {
    if (val === searchElement) {
      x = x + 1;
    }
  });
  return (x);
};
