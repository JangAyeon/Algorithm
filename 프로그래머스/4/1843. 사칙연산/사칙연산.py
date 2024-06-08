def solution(arr):
    ## 숫자는 문자형에서 숫자형으로 변환
    n = len(arr)
    max_dp = [[0 for _ in range(n)] for _ in range(n)]
    min_dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        if i%2==0:
            arr[i]=int(arr[i])
            max_dp[i][i]=min_dp[i][i]=arr[i]

    for x in range(3,n+1,2):
        for left in range(0,n,2):
            right = x+left-1
            
            if right>=n:
                break

            _max, _min=[],[]
            for op_idx in range(left+1, right,2):
                if arr[op_idx]=="+":
                    _max.append(max_dp[left][op_idx-1]+max_dp[op_idx+1][right])
                    _min.append(min_dp[left][op_idx-1]+min_dp[op_idx+1][right])
                elif arr[op_idx]=="-":
                    _max.append(max_dp[left][op_idx-1]-min_dp[op_idx+1][right])
                    _min.append(min_dp[left][op_idx-1]-max_dp[op_idx+1][right])
            min_dp[left][right]=min(_min)
            max_dp[left][right]=max(_max)
    

    answer =max_dp[0][-1]
    return answer