#!/usr/bin/node

const data = require('./100-data.js');

const occurrenceDict = data.dict;
const usersByOccurrence = {};

for (const userId in occurrenceDict) {
  if (!Object.prototype.hasOwnProperty.call(usersByOccurrence, occurrenceDict[userId])) {
    usersByOccurrence[occurrenceDict[userId]] = [];
  }

  usersByOccurrence[occurrenceDict[userId]].push(userId);
}
console.log(usersByOccurrence);
