import sys
input = sys.stdin.readline

T  = int(input())

for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        op, num = input().strip().split()
        if op == "I":
            arr.append(int(num))
        elif op=="D" and arr:
            if int(num) == -1:
                arr.remove(min(arr))
            elif int(num) == 1:
                arr.remove(max(arr))
        
    if arr:
        print(max(arr)," ",min(arr))
    else:
        print("EMPTY")
        