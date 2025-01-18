/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function (maze, entrance) {
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const [ROW, COL] = [maze.length, maze[0].length];
  const visited = new Array(ROW).fill(0).map((_) => new Array(COL).fill(false));
  console.log(visited);
  const MAX = 10 ** 5;
  let answer = 10 ** 5;
  const que = [[...entrance, 0]];
  visited[entrance[0]][entrance[1]] = true;
  while (que.length > 0) {
    const [r, c, dist] = que.shift();
    for (let [dr, dc] of dir) {
      let [nr, nc] = [r + dr, c + dc];
      if (!(0 <= nr && nr < ROW && 0 <= nc && nc < COL)) {
        console.log([r, nr, c, nc], dist, answer);
        if (r == entrance[0] && c == entrance[1] && dist <= 1) {
          continue;
        } else {
          //console.log(r, c, dist, answer)
          answer = Math.min(dist, answer);
          break;
        }
      } else if (visited[nr][nc] || maze[nr][nc] == "+") {
        continue;
      }
      que.push([nr, nc, dist + 1]);
      visited[nr][nc] = true;
    }
  }
  return answer === MAX ? -1 : answer;
};
