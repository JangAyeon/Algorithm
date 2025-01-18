/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function (grid) {
  const que = [];
  const dir = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  const [ROW, COL] = [grid.length, grid[0].length];
  let dist = 0;
  // const visited = new Array(ROW).fill(0).map((_)=>new Array(COL).fill(false))
  for (let i = 0; i < ROW; i++) {
    for (let j = 0; j < COL; j++) {
      if (grid[i][j] === 2) {
        que.push([i, j, dist]);
        grid[i][j] = 0;
      }
    }
  }
  // console.log(que)

  while (que.length > 0) {
    const [r, c, d] = que.shift();
    dist = Math.max(dist, d);
    for (let [dr, dc] of dir) {
      const [nr, nc] = [r + dr, c + dc];
      const isArea = 0 <= nr && nr < ROW && 0 <= nc && nc < COL;
      // 범위가 아님 || 이미 방문함
      if (!isArea || grid[nr][nc] === 0) {
        continue;
      } else if (grid[nr][nc] === 1) {
        grid[nr][nc] = 0;
        que.push([nr, nc, d + 1]);
      }
    }
  }
  console.log(grid.flat().includes(1), dist);
  return grid.flat().includes(1) ? -1 : dist;
};
