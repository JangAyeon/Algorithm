from collections import Counter
T = int(input())
for _ in range(T):
    ans=0
    idx = int(input())
    arr=Counter(list(map(int, input().split())))
    value = max(arr.values())
    for key in arr.keys():
        if arr[key]==value:
            ans = max(ans, key)
    string = '#{0} {1}'.format(idx,ans)
    print(string)