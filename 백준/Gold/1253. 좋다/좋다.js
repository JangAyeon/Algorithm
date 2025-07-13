const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => input.push(line)).on("close", () => {
  const N = +input[0];
  const arr = input[1].split(" ").map(Number).sort((a, b) => a - b);

  let goodCount = 0;

  for (let i = 0; i < N; i++) {
    const target = arr[i];
    let start = 0;
    let end = N - 1;

    while (start < end) {
              const sum = arr[start] + arr[end];
        if(sum==target){
            if(i!=start && i!=end){
                goodCount++
                break
            }
            else if(i==start){start++}
            else if (i==end){end--}
        }

 else if (sum < target) {
        start++;
      } else {
        end--;
      }
    }
  }

  console.log(goodCount);
});
