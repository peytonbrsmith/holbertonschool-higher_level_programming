#!/usr/bin/node
const list = require('./100-data').list;

console.log(list);

const newlist = list;
console.log(newlist.map(function (currentelement, index, arrayobj) {
  return currentelement * index;
}));
