/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function (equations, values, queries) {
  const n = equations.length;
  const graph = {};
  let answer = [];
  for (let i = 0; i < n; i++) {
    const [node1, node2] = equations[i];
    const v = values[i];
    if (graph[node1]) {
      graph[node1].push([node2, v]);
    } else {
      graph[node1] = [[node2, v]];
    }
    if (graph[node2]) {
      graph[node2].push([node1, 1 / v]);
    } else {
      graph[node2] = [[node1, 1 / v]];
    }
  }
  const keys = Object.keys(graph);

  for (let [start, end] of queries) {
    let flag = false;
    if (!keys.includes(start) || !keys.includes(end)) {
      answer.push(-1);
      // console.log(start, "->",end,": ",-1);
      continue;
    }
    const visited = new Set();
    const que = [[start, 1]];
    if (start == end) {
      // console.log(start, "->",end,": ",1);
      answer.push(1);
      continue;
    }
    while (que.length) {
      const [node, value] = que.shift();
      if (node == end) {
        // console.log(start, "->",end,": ",value);
        flag = true;
        answer.push(value);
        break;
      }
      for (let [next_, v] of graph[node]) {
        // console.log(node, next_,v)
        if (!visited.has(next_)) que.push([next_, value * v]);
        visited.add(next_);
      }
      // console.log(node, value)
    }
    if (!flag) {
      answer.push(-1);
    }
  }

  // console.log(answer)
  return answer;
};

/**
 *
 *  헷갈린 문법
 * Object.keys(graph)
 * map 문법
 *
 */
