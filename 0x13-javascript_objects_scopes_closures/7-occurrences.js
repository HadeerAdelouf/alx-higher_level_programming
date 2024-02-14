#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let numCount = 0;
  
    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        numCount++;
      }
    }
    return numCount;
  };
