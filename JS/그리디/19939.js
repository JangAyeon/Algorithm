// https://coder38611.tistory.com/114

let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split(" ");

let [n, k] = input.map(Number);
let ball = n - k;
let minBall = ((1 + k) * k) / 2;
if (minBall > n) {
  console.log(-1);
} else {
  let ball = n - minBall;
  if (ball % k == 0) {
    console.log(k - 1);
  } else {
    console.log(k);
  }
}
