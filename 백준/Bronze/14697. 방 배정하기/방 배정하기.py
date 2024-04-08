import sys
input = sys.stdin.readline


lst = list(map(int, input().split()))
arr, n = lst[:-1], lst[-1]
## print(arr, n)


"""
5 9 12 113
ans: 1  

2 3 4 13
ans: 1

1 2 3 300
ans: 1

3 6 9 112
ans: 0
"""


def sol(num, d, visited):
    ##print(num, d, visited)
    if num==0:
        print(1)
        exit() 
    elif sum(visited)==len(visited):
        return
    else:
        visited[arr.index(d)]=1
        for j in range(num//d+1):
            for i in range(len(arr)):
                if not(visited[i]):
                    ## print(num-d*j,j, d,visited)
                    visited[i]=1
                    sol(num-d*j,arr[i],visited)
                    visited[i]=0

       
for idx in range(len(arr)):
    sol(n, arr[idx], [0]*(len(arr)))
print(0)