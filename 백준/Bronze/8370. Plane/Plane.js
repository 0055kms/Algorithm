const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const [a,b,c,d] = input.map(Number);
console.log(a*b+c*d);