const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let input = [];

rl.on("line", (line) => input.push(line)).on("close", () => {
    const N = Number(input[0]);
    const arr = input[1].split(" ").map(Number);

    let swapCount = 0;

    function mergeSort(arr) {
        if (arr.length <= 1) return arr;

        const mid = Math.floor(arr.length / 2);
        const left = mergeSort(arr.slice(0, mid));
        const right = mergeSort(arr.slice(mid));

        let i = 0, j = 0;
        const sorted = [];

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                sorted.push(left[i++]);
            } else {
                sorted.push(right[j++]);
                // ⚠️ 오른쪽 원소가 왼쪽보다 작다는 건, 왼쪽에 있는 모든 남은 원소들이 역순 쌍
                swapCount += left.length - i;
            }
        }

        while (i < left.length) sorted.push(left[i++]);
        while (j < right.length) sorted.push(right[j++]);

        return sorted;
    }

    mergeSort(arr);
    console.log(swapCount);
});
