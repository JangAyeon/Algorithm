function dfs(visited, computers, curr) {
  visited[curr] = true;
  for (let idx = 0; idx < computers[curr].length; idx++) {
    // console.log(curr, idx, computers[curr][idx])
    if (idx != curr && computers[curr][idx] == 1 && visited[idx] == false) {
      dfs(visited, computers, idx);
    }
  }
}

function solution(n, computers) {
  var answer = 0;
  let visited = Array.from({ length: n }, () => false);
  for (let curr = 0; curr < n; curr++) {
    if (visited[curr] == false) {
      dfs(visited, computers, curr);
      answer++;
    }
  }
  return answer;
}
