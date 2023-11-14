#!/usr/bin/node
// find second largest number

let arr = process.argv; arr.shift(); arr.shift(); // remove first two items
arr = arr.map((item) => Number.parseInt(item, 10));
arr.sort((a, b) => b - a); // sort in ascending order
console.log(arr[1]);
