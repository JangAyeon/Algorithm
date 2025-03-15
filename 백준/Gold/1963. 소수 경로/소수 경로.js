const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function getPrimeNumbers() {
  const primes = new Array(10000).fill(true);
  primes[0] = primes[1] = false;
  for (let i = 2; i < 10000; i++) {
    if (primes[i]) {
      for (let j = i * i; j < 10000; j += i) {
        primes[j] = false;
      }
    }
  }
  return new Set([...Array(10000).keys()].filter((n) => n >= 1000 && primes[n]));
}

const primeSet = getPrimeNumbers();

function bfs(start, target) {
  if (start === target) return 0;

  const queue = [[start, 0]];
  const visited = new Set();
  visited.add(start);

  while (queue.length) {
    const [current, steps] = queue.shift();
    const strCurrent = current.toString();

    for (let i = 0; i < 4; i++) {
      for (let digit = 0; digit <= 9; digit++) {
        if (strCurrent[i] == digit) continue;

        const newNumber = parseInt(
          strCurrent.slice(0, i) + digit + strCurrent.slice(i + 1)
        );

        if (primeSet.has(newNumber) && !visited.has(newNumber)) {
          if (newNumber === target) return steps + 1;
          queue.push([newNumber, steps + 1]);
          visited.add(newNumber);
        }
      }
    }
  }
  return "Impossible";
}

let T;
const input = [];

rl.on("line", (line) => {
  if (!T) {
    T = parseInt(line);
  } else {
    input.push(line.split(" ").map(Number));
    if (input.length === T) {
      input.forEach(([a, b]) => console.log(bfs(a, b)));
      rl.close();
    }
  }
});
