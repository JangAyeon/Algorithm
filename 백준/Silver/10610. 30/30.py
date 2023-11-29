from itertools import permutations

arr = list(input())
numArr = list(map(int, arr))

## 10의 배수 불가능
if 0 not in numArr:
    print(-1)
## 3의 배수 불가능
elif sum(numArr)%3!=0:
    print(-1)
else:
    ## 3의 배수 가능하고 10의 배수 가능한 상태
    numArr.sort(reverse=True)
    sortedStrNum = list(map(str, numArr))
    print("".join(sortedStrNum))
    