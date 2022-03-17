N = int(input())
arr = [i for i in range(1, N+1)]
cnt = 0

for i in range(0, N+1):
    for j in range(i, N):
        print("### i = ", i, ", j = ", j)
        print(arr[i:j+1])
        if sum(arr[i:j+1]) == N:
            cnt += 1
print(cnt)
