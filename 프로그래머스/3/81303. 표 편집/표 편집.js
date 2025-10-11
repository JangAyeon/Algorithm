class Node {
  constructor() {
    this.removed = false;
    this.prev = null;
    this.next = null;
  }
}

function solution(n, k, cmds) {
  const nodes = Array.from({ length: n }, () => new Node());
  let curr = nodes[k];
  const stack = [];

  // 연결 리스트 구성
  for (let i = 1; i < n; i++) {
    nodes[i - 1].next = nodes[i];
    nodes[i].prev = nodes[i - 1];
  }

  for (const cmd of cmds) {
    const [c, num] = cmd.split(" ");

    if (c === "D") {
      let step = Number(num);
      for (let i = 0; i < step; i++) curr = curr.next;
    } 
    else if (c === "U") {
      let step = Number(num);
      for (let i = 0; i < step; i++) curr = curr.prev;
    } 
    else if (c === "C") {
      stack.push(curr);
      curr.removed = true;

      const up = curr.prev;
      const down = curr.next;

      if (up) up.next = down;
      if (down) {
        down.prev = up;
        curr = down;
      } else {
        curr = up;
      }
    } 
    else if (c === "Z") {
      const item = stack.pop();
      item.removed = false;

      const up = item.prev;
      const down = item.next;

      if (up) up.next = item;
      if (down) down.prev = item;
    }
  }

  return nodes.map(node => (node.removed ? "X" : "O")).join("");
}
