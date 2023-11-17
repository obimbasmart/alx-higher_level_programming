#!/usr/bin/node
// reverse an array

exports.esrever = function (list) {
  return reverseList(list);
};

function reverseList (list) {
  if (!list.length) {
    return list;
  }

  return reverseList(list.slice(1)).concat(list[0]);
}
