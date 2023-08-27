// day 5: 이진수 정렬

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", (line) => {
  const string = line.trim().split(" ").map(Number);
  //console.log(string)
  input.push(string);
  if (input.length == 2) {
    rl.close();
  }
});

function getBinary(arr) {
  let binArr = [];
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i];
    const binCount = num
      .toString(2)
      .split("")
      .filter((element) => element == "1").length;
    binArr.push([binCount, num]);
  }
  return binArr;
}

function sortBin(a, b) {
  if (b[0] - a[0] != 0) {
    return b[0] - a[0];
  } else {
    return b[1] - a[1];
  }
}

rl.on("close", () => {
  //console.log("Hello Goorm! Your input is " + input);
  const [n, k] = input[0];
  const arr = input[1];
  const binArr = getBinary(arr);
  const sortedBinArr = binArr.sort(sortBin);
  //console.log(n,k);
  //console.log(arr);
  //console.log(binArr);
  //console.log(sortedBinArr);
  const answer = sortedBinArr[k - 1][1];
  console.log(answer);
  process.exit();
});
