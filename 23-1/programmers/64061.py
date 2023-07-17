def solution(board, moves):
    
    bucket = []
    count = 0
    
    for i in moves:
        for j in range(len(board[i-1])):
            num = board[j][i-1]
            
            if num !=0:
                bucket.append(num)
                board[j][i-1]=0
                
                if len(bucket)>1:
                    if bucket[-1]==bucket[-2]:
                        bucket.pop(-1)
                        bucket.pop(-1)
                        count+=2
                break
    
    return count
    