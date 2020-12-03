#!/usr/bin/env node
const fs = require('fs');

const passwordsWithPolicies = fs
  .readFileSync(0, 'utf-8')
  .trim()
  .split('\n')
  .map((line) => {
    const [policy, password] = line.split(':').map((x) => x.trim());
    const [range, letter] = policy.split(' ');
    const [firstNumber, secondNumber] = range
      .split('-')
      .map((x) => parseInt(x));
    return { password, policy: { letter, firstNumber, secondNumber } };
  });

const firstCorrect = passwordsWithPolicies.filter(({ password, policy }) => {
  const count = password.match(new RegExp(policy.letter, 'g'))?.length || 0;
  return policy.firstNumber <= count && count <= policy.secondNumber;
});

const secondCorrect = passwordsWithPolicies.filter(({ password, policy }) => {
  const pos1 = password[policy.firstNumber - 1] == policy.letter;
  const pos2 = password[policy.secondNumber - 1] == policy.letter;
  return (pos1 && !pos2) || (!pos1 && pos2);
});

console.log(firstCorrect.length);
console.log(secondCorrect.length);
