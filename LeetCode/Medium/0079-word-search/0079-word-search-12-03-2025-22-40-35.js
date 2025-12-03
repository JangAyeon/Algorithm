/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const [N,M] = [board.length, board[0].length]
    for(let i=0;i<N;i++){
        for(let j=0;j<M;j++){
            if(dfs(i,j,0)){return true}
        }
    }
    function dfs(r,c, idx){
        if(idx>=word.length){return true}
        if(r<0 || r>=N || c<0 || c>=M || board[r][c]!=word[idx]){return false}
        const temp = board[r][c]
        board[r][c]="."
        const found = dfs(r-1,c, idx+1) || dfs(r+1,c, idx+1) || dfs(r,c+1, idx+1) || dfs(r, c-1, idx+1)
        board[r][c] = temp
        return found


   }
   return false
    
};