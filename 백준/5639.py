import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

arr = []
while True:
    try:
        arr.append(int(input().strip()))
    except:
        break
#print(arr)

def postOrder(subTree):
    if len(subTree) == 0:
        return
    tempL, tempR = [], []
    mid = subTree[0] # 루트
    # 루트보다 커지는 곳 찾기
    flag = False
    for i in range(1, len(subTree)):
        if subTree[i]>=mid:
            tempL = subTree[1:i] # idx : 1 ~ i-1
            tempR = subTree[i:] # idx : i ~
            flag = True
            break

    if not flag: # 루트보다 커지는 경우 없음
        tempL = subTree[1:]

    postOrder(tempL)
    postOrder(tempR)
    print(mid)


postOrder(arr)