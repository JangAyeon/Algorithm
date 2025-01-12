/**
 * @param {number[][]} isConnected
 * @return {number}
 */

function getAdj(isConnected, size) {
  const adj = new Array(size).fill([]).map((_) => []);
  //console.log(adj)
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      // console.log(i,j, isConnected[i][j])
      if (i !== j && isConnected[i][j]) {
        adj[i].push(j);
      }
    }
  }
  //console.log("adj", adj)
  return adj;
}

function dfs(node, visited, adj) {
  //if(){return}
  for (next_ of adj[node]) {
    if (!visited[next_]) {
      visited[next_] = true;
      dfs(next_, visited, adj);
    }
  }
}

var findCircleNum = function (isConnected) {
  const size = isConnected.length;
  const adj = getAdj(isConnected, size);
  const visited = new Array(size).fill(false);
  let answer = 0;
  for (let node = 0; node < size; node++) {
    if (!visited[node]) {
      //console.log(node)
      answer += 1;
      dfs(node, visited, adj);
    }
  }

  return answer;
};
