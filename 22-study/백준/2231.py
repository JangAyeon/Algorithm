N = int(input())


for i in range(1, N+1):
    #print("i", i, "split", list(map(int, str(i))))
    total = i+sum(map(int, str(i)))
    #print("total", total)
    if total == N:
        print(i)
        break
    if i == N:
        print(0)
