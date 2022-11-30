#!/usr/bin/node

/* returns the reversed version of a list */
exports.esrever = function (list) {
  let myList = list;
  const newList = [];
  for (let n = myList.length - 1; n >= 0; n--) {
    newList.push(myList[n])
  }
  return (newList)
};
