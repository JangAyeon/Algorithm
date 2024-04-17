import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr=[1,5,10,50]


sum_set = set()

def dfs(idx,ans_list):

    if len(ans_list) == n:
        sum_set.add(sum(ans_list))
        return

    for i in range(idx,4):
        #ans_list.append(arr[i])
        dfs(i, ans_list+[arr[i]])
        #ans_list.pop()

dfs(0,[])

print(len(sum_set))