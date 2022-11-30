#!/usr/bin/node

/* convert from base 10 to other bases */
exports.converter = function (base) {
  function myConverter (x) {
    return x.toString(base);
  }
  return myConverter;
};
