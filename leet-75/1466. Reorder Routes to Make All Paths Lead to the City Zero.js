/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */

function getList(n, connections) {
  const adj = new Array(n).fill([]).map(() => []); // 양방향
  const arrow = new Array(n).fill([]).map(() => []); // 단방향
  for (let e of connections) {
    const [a, b] = e;
    adj[a].push(b);
    adj[b].push(a);
    arrow[a].push(b);
  }
  return { adj, arrow };
}

var minReorder = function (n, connections) {
  const { adj, arrow } = getList(n, connections);
  const visited = new Array(n).fill(false);
  console.log(adj, arrow);
  let count = 0;
  function dfs(node, adj, arrow, visited) {
    for (let next_ of adj[node]) {
      if (!visited[next_]) {
        console.log(node, next_);
        if (!arrow[next_].includes(node)) {
          console.log(next_, "->", node, " 없음");
          count += 1;
        }
        visited[next_] = true;
        dfs(next_, adj, arrow, visited, count);
      }
    }
  }
  visited[0] = true;
  dfs(0, adj, arrow, visited);
  console.log(count);
  return count;
};
