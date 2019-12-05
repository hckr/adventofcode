#!/usr/bin/env node
const fs = require('fs');

const program = fs
    .readFileSync(0, 'utf-8')
    .trim()
    .split(',')
    .map(x => parseInt(x));

// part one
console.log(execute(program, [1]).join(', '));

// part two
console.log(execute(program, [5]).join(', '));


function execute(program, input) {
    const memory = [...program];
    const localInput = [...input];
    const localOutput = [];
    let ip = 0;

    while (true) {
        const instruction = memory[ip];
        const opcode = instruction % 100;
        const argMode1 = Math.floor(instruction / 100) % 10;
        const argMode2 = Math.floor(instruction / 1000) % 10;
        const arg1Val = argMode1 === 0 ? memory[memory[ip + 1]] : memory[ip + 1];
        const arg2Val = argMode2 === 0 ? memory[memory[ip + 2]] : memory[ip + 2];

        switch (opcode) {
            case 1:
                memory[memory[ip + 3]] = arg1Val + arg2Val;
                ip += 4;
                break;
            case 2:
                memory[memory[ip + 3]] = arg1Val * arg2Val;
                ip += 4;
                break;
            case 3:
                memory[memory[ip + 1]] = localInput.shift();
                ip += 2;
                break;
            case 4:
                localOutput.push(arg1Val);
                ip += 2;
                break;
            case 5:
                if (arg1Val !== 0) {
                    ip = arg2Val;
                } else {
                    ip += 3;
                }
                break;
            case 6:
                if (arg1Val === 0) {
                    ip = arg2Val;
                } else {
                    ip += 3;
                }
                break;
            case 7:
                memory[memory[ip + 3]] = arg1Val < arg2Val ? 1 : 0;
                ip += 4;
                break;
            case 8:
                memory[memory[ip + 3]] = arg1Val === arg2Val ? 1 : 0;
                ip += 4;
                break;
            case 99:
                return localOutput;
            default:
                throw new Error(`Unknown opcode: ${opcode}`);
        }
    }
}
