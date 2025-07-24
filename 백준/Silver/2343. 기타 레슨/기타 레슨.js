const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout

})

const input = []
rl.on("line", line => input.push(line)).on("close", () => {



    const [N, M] = input[0].split(" ").map(Number)
    const arr = input[1].split(" ").map(Number)
    let start = Math.max(...arr)
    let end = arr.reduce((acc, item) => (acc += item), 0)

    let answer = end
    // console.log(N, M, arr)


 function getCount(size) {
  let count = 1; // 블루레이 최소 1개
  let sum = 0;

  for (let i = 0; i < N; i++) {
    if (sum + arr[i] > size) {
      count++;
      sum = arr[i]; // 새 블루레이 시작
    } else {
      sum += arr[i];
    }
  }

  return count;
}

    function bisect() {


        while (start <= end) {

            let target = parseInt((start + end) / 2)
            let count = getCount(target)
            // console.log("(answer, count, target, start, end)", answer, count, target, start, end)
            if (count <= M) {

                answer = Math.min(answer, target)
                end = target - 1
            } else {
                start = target + 1
            }

        }
        console.log(start)

    }
    bisect()
})