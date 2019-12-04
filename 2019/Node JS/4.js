#!/usr/bin/env node
const fs = require('fs');

const [rangeMin, rangeMax] = fs
    .readFileSync(0, 'utf-8')
    .trim()
    .split('-');

let possiblePasswords = 0;
let actualPossiblePasswords = 0;

for (let p = rangeMin; p <= rangeMax; ++p) {
    const password = p.toString();
    if (satisfiesCriteria(password)) {
        possiblePasswords += 1;
    }
    if (satisfiesActualCriteria(password)) {
        actualPossiblePasswords += 1;
    }
}

// part one
console.log(possiblePasswords);

// part two
console.log(actualPossiblePasswords);

function satisfiesCriteria(password) {
    let hasTwoSameAdjacent = false;
    for (let i = 0; i < password.length - 1; ++i) {
        if (password[i + 1] < password[i]) {
            return false;
        }
        if (password[i] === password[i + 1]) {
            hasTwoSameAdjacent = true;
        }
    }
    return hasTwoSameAdjacent;
}

function satisfiesActualCriteria(password) {
    for (let i = 0; i < password.length - 1; ++i) {
        if (password[i + 1] < password[i]) {
            return false;
        }
    }
    return (password.match(/(\d)\1+/g) || []).map(g => g.length).includes(2);
}
