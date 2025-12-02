var exist = function(board, word) {
    const N = board.length;
    const M = board[0].length;

    function dfs(r, c, idx) {
        // 단어 완성
        if (idx === word.length) return true;
        // 경계 + 글자 불일치
        if (r < 0 || c < 0 || r >= N || c >= M || board[r][c] !== word[idx]) return false;

        // 방문 표시
        const temp = board[r][c];
        board[r][c] = "#";

        const found =
            dfs(r+1, c, idx+1) ||
            dfs(r-1, c, idx+1) ||
            dfs(r, c+1, idx+1) ||
            dfs(r, c-1, idx+1);

        // 방문 복구 (Backtracking)
        board[r][c] = temp;

        return found;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (dfs(i, j, 0)) return true;
        }
    }

    return false;
};
