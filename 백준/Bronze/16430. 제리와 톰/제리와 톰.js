const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
let [A,B] = input.map(Number);
console.log(B-A);
console.log(B);