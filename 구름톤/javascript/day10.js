// day10: GameJam

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const directions = {
  U: [-1, 0],
  D: [1, 0],
  L: [0, -1],
  R: [0, 1],
};

let N;
let goormPos, playerPos;
let goormVisited, playerVisited;
let board = [];

function set_Pos(a) {
  if (a === -1) return N - 1;
  if (a === N) return 0;
  return a;
}

function move(pos, visited, score, board) {
  let [x, y] = pos;
  visited[x][y] = true;
  let flag = true;

  while (flag) {
    let command = board[x][y];
    let distance = parseInt(command.slice(0, -1));
    let direction = command.slice(-1);

    for (let i = 0; i < distance; i++) {
      x += directions[direction][0];
      y += directions[direction][1];
      x = set_Pos(x);
      y = set_Pos(y);
      if (!visited[x][y]) {
        visited[x][y] = true;
        score += 1;
      } else {
        flag = false;
        break;
      }
    }
  }
  return score;
}

let input = [];
rl.on("line", (line) => {
  input.push(line);
  N = Number(input[0]);
  if (input.length === N + 3) {
    rl.close();
  }
});

function getStart(start) {
  // split and make 1-index to 0-index
  const pos = start.split(" ").map((num) => Number(num) - 1);
  return pos;
}

function getBoard() {
  for (let i = 3; i < N + 3; i++) {
    board.push(input[i].split(" "));
  }
}

function createVisited() {
  return Array.from(Array(N), () => new Array(N).fill(false));
}

rl.on("close", () => {
  goormPos = getStart(input[1]);
  goormVisited = createVisited();
  playerPos = getStart(input[2]);
  playerVisited = createVisited();
  getBoard();

  let goormScore = move(goormPos, goormVisited, 1, board);
  let playerScore = move(playerPos, playerVisited, 1, board);

  if (goormScore > playerScore) {
    console.log("goorm " + goormScore);
  } else if (goormScore < playerScore) {
    console.log("player " + playerScore);
  }
  process.exit();
});
