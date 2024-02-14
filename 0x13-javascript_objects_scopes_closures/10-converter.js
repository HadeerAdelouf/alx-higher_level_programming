#!/usr/bin/node

exports.converter = function (base) {
  return function (nUm) {
    return nUm.toString(base);
  };
};
