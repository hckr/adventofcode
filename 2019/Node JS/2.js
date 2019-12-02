#!/usr/bin/env node
const fs = require('fs');

const program = fs
    .readFileSync(0, 'utf-8')
    .trim()
    .split(',')
    .map(x => parseInt(x));

function execute(program, noun, verb) {
    const p = [...program];
    if (noun !== undefined) {
        p[1] = noun;
    }
    if (verb !== undefined) {
        p[2] = verb;
    }

    let ip = 0;
    while (true) {
        switch (p[ip]) {
            case 1:
                p[p[ip + 3]] = p[p[ip + 1]] + p[p[ip + 2]];
                break;
            case 2:
                p[p[ip + 3]] = p[p[ip + 1]] * p[p[ip + 2]];
                break;
            case 99:
                return p;
        }
        ip += 4;
    }
}

// part one
console.log(execute(program, 12, 2)[0]);

// part two
const expectedValue = 19690720;
for (let noun = 0; noun < 100; ++noun) {
    for (let verb = 0; verb < 100; ++verb) {
        if (execute(program, noun, verb)[0] === expectedValue) {
            console.log(100 * noun + verb);
        }
    }
}
