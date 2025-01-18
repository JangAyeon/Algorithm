/**
 * @param {number[][]} grid
 * @return {number}
 */

function swap(grid) {
  const newGrid = new Map();
  for (let r = 0; r < grid.length; r++) {
    let key = "";
    for (let c = 0; c < grid.length; c++) {
      key = c == 0 ? key + grid[c][r] : key + "_" + grid[c][r];
    }
    const value = newGrid.has(key) ? newGrid.get(key) + 1 : 1;
    newGrid.set(key, value);
  }
  return newGrid;
}
var equalPairs = function (grid) {
  const count = swap(grid);
  let answer = 0;
  for (let r of grid) {
    const key = r.join("_");
    answer += count.has(key) ? count.get(key) : 0;
  }
  //console.log(count)
  return answer;
};
