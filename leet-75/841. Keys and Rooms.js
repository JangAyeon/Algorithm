/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
  const visited = Array.from({ length: rooms.length }, () => false);
  const c = rooms[0];
  const keys = [...c];
  visited[0] = true;
  //console.log(keys, visited,c)

  while (keys.length > 0) {
    const k = keys.shift();
    visited[k] = true;
    for (let r of rooms[k]) {
      if (!visited[r]) {
        keys.push(r);
      }
    }
    //console.log("###",  visited, keys)
  }

  //console.log(visited)
  return visited.includes(false) ? false : true;
};
