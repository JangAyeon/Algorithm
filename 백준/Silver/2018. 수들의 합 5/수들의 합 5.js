const readline = require("readline")
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

const input = []
rl.on("line", line =>input.push(line)).on("close", ()=>{

const N = +input[0];

let count = 0;
let start = 1;
let end = 1;
let total = 1;

while (end <= N) {
  if (total < N) {
    end++;
    total += end;
  } else if (total === N) {
    count++;
    end++;
    total += end;
  } else {
    total -= start;
    start++;
  }
}

console.log(count);

})