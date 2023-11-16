// 배열로 구현
function bfs(graph, start, visited){
  que = new Array();
  que.push(start);
  visited[start]=true
  while(que.length!=0){
    node = que.pop();
    console.log(node)
    for(next_ of graph[node]){
      if(!visited[next_]){
        que.push(next_);
        visited[next_]=true
      }
    }
  }
}

// 각 노드가 연결된 정보
graph =[
  [],
  [2,3,4],
  [1],
  [1,5,6],
  [1,7],
  [3,8],
  [3],
  [4],
  [5]
]

// 각 노드가 방문된 정보 표현
visited = Array(graph.length).fill(false)

// bfs 함수 호출
bfs(graph, 1, visited)