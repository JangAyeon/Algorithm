def solution(arr):
    n = len(arr)
    max_dp =[[0 for _ in range(n)] for _ in range(n)]
    min_dp =[[0 for _ in range(n)] for _ in range(n)]
    for idx in range(n):
        if arr[idx] not in ["-","+"]:
            arr[idx] = max_dp[idx][idx] = min_dp[idx][idx] = int(arr[idx])
    
    for gap in range(3, n+1, 2):
        for start in range(0, n,2):
            end = start+gap-1
            if end>=n:
                break
            max_, min_ =  [],[]
            for op in range(start+1, end, 2):
                if arr[op]=="+":
                    max_.append(max_dp[start][op-1]+max_dp[op+1][end])
                    min_.append(min_dp[start][op-1]+min_dp[op+1][end])
                elif arr[op]=="-":
                    max_.append(max_dp[start][op-1]-min_dp[op+1][end])
                    min_.append(min_dp[start][op-1]-max_dp[op+1][end])
            max_dp[start][end]=max(max_)
            min_dp[start][end]=min(min_)
    answer = (max_dp[0][-1])
    return answer