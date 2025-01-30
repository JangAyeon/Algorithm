const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];

function getSum(type, graph, r, c) {
  if (type === 1) {
    //console.log(graph[r][c] , graph[r][c + 1] , graph[r][c + 2] , graph[r][c + 3])
    return graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r][c + 3];
  } else if (type == 2) {
    //console.log(graph[r][c] , graph[r + 1][c] , graph[r + 2][c] , graph[r + 3][c])
    return graph[r][c] + graph[r + 1][c] + graph[r + 2][c] + graph[r + 3][c];
  } else if (type === 3) {
    //console.log(graph[r][c] , graph[r + 1][c] , graph[r][c + 1] , graph[r + 1][c + 1])
    return (
      graph[r][c] + graph[r + 1][c] + graph[r][c + 1] + graph[r + 1][c + 1]
    );
  } else if (type === 4) {
    return (
      graph[r][c] + graph[r][c + 1] + graph[r + 1][c + 1] + graph[r + 1][c + 2]
    );
  } else if (type == 5) {
    return (
      graph[r][c + 1] + graph[r + 1][c] + graph[r + 1][c + 1] + graph[r + 2][c]
    );
  } else if (type === 6) {
    return (
      graph[r][c] + graph[r][c + 1] + graph[r][c + 2] + graph[r + 1][c + 1]
    );
  } else if (type === 7) {
    //console.log(graph[r][c + 1] , graph[r + 1][c] , graph[r + 1][c + 1] , graph[r + 2][c + 1])
    return (
      graph[r][c + 1] +
      graph[r + 1][c] +
      graph[r + 1][c + 1] +
      graph[r + 2][c + 1]
    );
  } else if (type === 8) {
    //console.log(graph[r][c + 1] , graph[r + 1][c] , graph[r + 1][c + 1] , graph[r + 1][c + 2])
    return (
      graph[r][c + 1] +
      graph[r + 1][c] +
      graph[r + 1][c + 1] +
      graph[r + 1][c + 2]
    );
  } else if (type === 9) {
    return (
      graph[r][c] + graph[r + 1][c + 1] + graph[r + 1][c] + graph[r + 2][c]
    );
  } else if (type === 10) {
    return (
      graph[r][c] + graph[r + 1][c + 2] + graph[r][c + 1] + graph[r][c + 2]
    );
  } else if (type === 11) {
    return (
      graph[r][c + 1] +
      graph[r + 1][c + 1] +
      graph[r + 2][c] +
      graph[r + 2][c + 1]
    );
  } else if (type === 12) {
    return (
      graph[r][c] + graph[r + 1][c] + graph[r + 1][c + 1] + graph[r + 1][c + 2]
    );
  } else if (type === 13) {
    return graph[r][c] + graph[r][c + 1] + graph[r + 1][c] + graph[r + 2][c];
  }
}

function getType(r, c, N) {
  const types = [];

  if (c < N - 3) {
    types.push(1);
  }
  if (r < N - 3) {
    types.push(2);
  }
  if (r < N - 2) {
    if (c < N - 2) {
      //types.push(4);
    }
    if (c < N - 1) {
      types.push(5);
      types.push(7);
      types.push(9);
      types.push(11);
      types.push(13);
    }
  }

  if (r < N - 1) {
    if (c < N - 2) {
      types.push(8);
      types.push(6);
      types.push(4);
      types.push(10);
      types.push(12);
    }
    if (c < N - 1) {
      types.push(3);
    }
  }

  //console.log(types)
  return types;
}

rl.on("line", (line) => {
  const n = line.trim();
  if (n === "0") {
    rl.close();
  }
  lines.push(n);
}).on("close", () => {
  let t = 0;

  while (lines.length > 1) {
    t += 1;
    let answer = -Infinity;
    const N = Number(lines.shift());
    const graph = [];
    for (let i = 0; i < N; i++) {
      const r = lines
        .shift()
        .split(" ")
        .filter((e) => e.length > 0);
      graph.push(r.map(Number));
    }
    //console.log("=====", t, "=====");
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < N; j++) {
        //console.log("=========================");
        //console.log("i: ", i, ", j: ", j);
        const types = getType(i, j, N);

        types.forEach((type) => {
          const total = getSum(type, graph, i, j);
          //console.log(type, ": ", total);

          answer = Math.max(answer, total);
        });
        //console.log("=========================");
      }
    }

    //console.log(N)
    //console.log(graph)
    console.log(`${t}.`, answer);
  }
});
