#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  list.forEach((item) => {
    newlist.unshift(item);
  });
  return (newlist);
};
