const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const lines = []

rl.on(("line"), (line) => {

    lines.push(line.trim())


}).on(("close"), () => {
    const N = Number(lines[0])
    const arr = lines.slice(1).map((r) => r.split(" ").map(Number))

    let answer = 0


    function move(board, dir) {
        let n = board.length;
        if (dir === 0) { // 동쪽 (오른쪽)
            for (let i = 0; i < n; i++) {
                let spot = n - 1; // 가장 오른쪽
                for (let j = n - 2; j >= 0; j--) {
                    if (board[i][j]) {
                        let tmp = board[i][j];
                        board[i][j] = 0;
                        if (board[i][spot] === 0) {
                            board[i][spot] = tmp;
                        } else if (board[i][spot] === tmp) {
                            board[i][spot] = tmp * 2;
                            spot--;
                        } else {
                            spot--;
                            board[i][spot] = tmp;
                        }
                    }
                }
            }
        } else if (dir === 1) { // 서쪽 (왼쪽)
            for (let i = 0; i < n; i++) {
                let spot = 0; // 가장 왼쪽
                for (let j = 1; j < n; j++) {
                    if (board[i][j]) { // 0이 아닌 값이
                        let tmp = board[i][j];
                        board[i][j] = 0; // 일단 해당 칸은 이동하니까 0으로
                        if (board[i][spot] === 0) { // 비어있으면
                            board[i][spot] = tmp; // 옮김
                        } else if (board[i][spot] === tmp) { // 같으면
                            board[i][spot] = tmp * 2; // 합친다
                            spot++;
                        } else { // 비어있지 않고 다른 값일때
                            spot++; // pass
                            board[i][spot] = tmp; // 바로 옆에 붙임
                        }
                    }
                }
            }
        } else if (dir === 2) { // 남쪽 (아래)
            for (let j = 0; j < n; j++) {
                let spot = n - 1;
                for (let i = n - 2; i >= 0; i--) {
                    if (board[i][j]) {
                        let tmp = board[i][j];
                        board[i][j] = 0;
                        if (board[spot][j] === 0) {
                            board[spot][j] = tmp;
                        } else if (board[spot][j] === tmp) {
                            board[spot][j] = tmp * 2;
                            spot--;
                        } else {
                            spot--;
                            board[spot][j] = tmp;
                        }
                    }
                }
            }
        } else { // 북쪽 (위)
            for (let j = 0; j < n; j++) {
                let spot = 0;
                for (let i = 1; i < n; i++) {
                    if (board[i][j]) {
                        let tmp = board[i][j];
                        board[i][j] = 0;
                        if (board[spot][j] === 0) {
                            board[spot][j] = tmp;
                        } else if (board[spot][j] === tmp) {
                            board[spot][j] = tmp * 2;
                            spot++;
                        } else {
                            spot++;
                            board[spot][j] = tmp;
                        }
                    }
                }
            }
        }
        return board;
    }




    function dfs(board, count) {
        if (count === 5) {
            for (let r = 0; r < N; r++) {

                for (let c = 0; c < N; c++) {

                    answer = Math.max(answer, board[r][c])
                }
            }
            return

        }

        for (let i = 0; i < 4; i++) {
            const newBoard = board.map(r => [...r])
            moved_board = move(newBoard, i)
            dfs(moved_board, count + 1)


        }



    }
    dfs(arr, 0)
    console.log(answer)
})