#!/usr/bin/env node
const fs = require('fs');

const entries = fs
  .readFileSync(0, 'utf-8')
  .trim()
  .split('\n')
  .map((x) => parseInt(x));

let firstSolution = null;
let secondSolution = null;

for (let i = 0; i < entries.length; ++i) {
  const first = entries[i];

  for (let j = i + 1; j < entries.length; ++j) {
    const second = entries[j];

    if (first + second == 2020) {
      firstSolution = first * second;
    }

    for (let k = j + 1; k < entries.length; ++k) {
      const third = entries[k];

      if (first + second + third == 2020) {
        secondSolution = first * second * third;
      }
    }
  }
}

console.log(firstSolution);
console.log(secondSolution);
