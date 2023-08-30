// day 8: 통증 

const readline = require("readline");
let rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let n;
const item = [14, 7, 1];
rl.on("line", (line) => {
  n = Number(line);
  rl.close();
});

function getItemCount(pain) {
  let use = 0;
  for (let i = 0; i < item.length; i++) {
    use += Math.floor(pain / item[i]);
    pain = pain % item[i];
  }
  return use;
}

rl.on("close", () => {
  const answer = getItemCount(n);
  console.log(answer);
  process.exit();
});
