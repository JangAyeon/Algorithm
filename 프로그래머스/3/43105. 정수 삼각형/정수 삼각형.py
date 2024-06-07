def solution(triangle):
 
    n = len(triangle)

    dp = [[triangle[0][0]]]

    for r in range(1,n):
        temp = [dp[-1][0]+triangle[r][0]]
        for c in range(1, r):
            node = triangle[r][c]
            temp.append(node+max(dp[-1][c-1], dp[-1][c]))
        ##temp.append(dp[r-1][-1]+triangle[r][0])
        temp.append(dp[-1][-1]+triangle[r][-1])
        dp.append(temp)

    answer = max(dp[-1])
    return answer