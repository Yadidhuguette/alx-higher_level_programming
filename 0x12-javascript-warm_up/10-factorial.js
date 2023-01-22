#!/usr/bin/node
function factorial (i) {
const number = parseInt(i);
if (isNaN(number)) {
return 1;
}
if (i === 0) {
return 1;
}
return i * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
