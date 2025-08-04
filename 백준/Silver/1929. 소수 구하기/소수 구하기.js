const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const lines = [];
rl.on("line", (line) => lines.push(line)).on("close", () => {
    const [M, N] = lines[0].split(" ").map(Number);
    const isNotPrime = Array(N + 1).fill(false);
    isNotPrime[0] = true;
    isNotPrime[1] = true;

    for (let i = 2; i * i <= N; i++) {
        if (!isNotPrime[i]) {
            for (let j = i * i; j <= N; j += i) {
                isNotPrime[j] = true;
            }
        }
    }

    const result = [];
    for (let i = M; i <= N; i++) {
        if (!isNotPrime[i]) result.push(i);
    }

    console.log(result.join("\n"));
});
