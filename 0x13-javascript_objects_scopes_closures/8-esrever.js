#!/usr/bin/node

/* returns the reversed version of a list */

exports.esrever = function (list) {
  const newList = [];
  for (let n = list.length - 1; n >= 0; n--) {
    newList.push(list[n]);
  }
  return (newList);
};
