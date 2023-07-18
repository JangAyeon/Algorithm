def solution(board, moves):
    answer = 0
    
    stack = []
    for move in moves:
        for row in range(len(board[move-1])):
            col = move-1
            num = board[row][col]
            if num!=0:
                board[row][col]=0
                stack.append(num)
                if len(stack)>1 and stack[-2]==stack[-1]:
                    stack.pop(-1)
                    stack.pop(-1)
                    answer+=2
                break
    
    
    
    return answer