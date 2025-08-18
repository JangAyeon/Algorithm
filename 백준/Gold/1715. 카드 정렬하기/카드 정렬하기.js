const readline = require("readline")

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})
class PriorityQueue {
    constructor() {
        this.heap = [];
    }

    swap(a, b) {
        const temp = this.heap[a];
        this.heap[a] = this.heap[b];
        this.heap[b] = temp;
    }

    push(value) {
        const {
            heap
        } = this;
        heap.push(value);
        let index = heap.length - 1;
        let parent = Math.floor((index - 1) / 2);

        while (index > 0 && heap[index] < heap[parent]) {
            this.swap(index, parent);
            index = parent;
            parent = Math.floor((index - 1) / 2);
        }
    }

    pop() {
        const {
            heap
        } = this;
        if (heap.length <= 1) {
            return heap.pop();
        }

        const output = heap[0];
        heap[0] = heap.pop();
        let index = 0;

        while (index * 2 + 1 < heap.length) {
            let left = index * 2 + 1;
            let right = index * 2 + 2;
            let next = index;

            if (heap[left] < heap[next]) {
                next = left;
            }

            if (right < heap.length && heap[right] < heap[next]) {
                next = right;
            }

            if (index === next) {
                break;
            }

            this.swap(index, next);
            index = next;
        }

        return output;
    }
}
const lines = []
rl.on("line", line => lines.push(line)).on("close", () => {
    const N = +lines[0]
    const arr = lines.slice(1).map(Number)
    let answer = 0
    const que = new PriorityQueue()
    arr.forEach((item) => que.push(item))
    while (que.heap.length > 1) {
        const sum = que.pop() + que.pop();
        que.push(sum);
        answer += sum;
    }
    console.log(answer)

})