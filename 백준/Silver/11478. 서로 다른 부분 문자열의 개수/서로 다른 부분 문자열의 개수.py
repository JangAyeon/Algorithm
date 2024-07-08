
import sys
input=sys.stdin.readline

arr = list(input().strip())
n = len(arr)
result= set()




for start in range(n):
    for end in range(start, n):
        w = "".join(arr[start:end+1])
        result.add(w)
print(len(result))