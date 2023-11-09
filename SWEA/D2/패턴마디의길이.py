from collections import Counter

T = int(input())
for idx in range(T):
    word = input()
    max_length = 10
    ans = max_length
    for unit in range(max_length,0, -1):
        string = word[:len(word)-len(word)%unit]
        b = set([string[i : i + unit] for i in range(0,len(string),unit)])
        if len(b)==1:
            ans = min(ans, unit)

    print('#{0} {1}'.format(idx+1,ans))