import sys
input = sys.stdin.readline

arr = []
n = 0
for idx in range(5):
    lst = input().strip()
    n = max(n, len(lst))
    arr.append(lst)


answer = ""

for row in range(5):
    if len(arr[row])<n:
        arr[row]+="."*(n-len(arr[row]))

for col in range(n):
    for row in range(5):
        if arr[row][col]!=".":
            answer+=arr[row][col]


print(answer)