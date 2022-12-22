#!/usr/bin/node
function factorial (f) {
if (isNaN(f) || f < 2) {
return 1;
} else {
return f * factorial(f - 1);
}
}
console.log(factorial(process.argv[2]));
