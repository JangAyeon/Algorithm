from collections import Counter

def checkRow(arr):
    for i in arr:
        count = Counter(i)
        if not checkCount(count):
            return False
    return True

def checkCol(arr):
    for i in range(len(arr)):
        temp=[]
        for row in arr:
            temp.append(row[i])

        count = Counter(temp)
        #print(set(count.values()),count,temp)
        if not checkCount(temp):
            return False
    return True
            

def checkCount(arr):
    count = Counter(arr)
    if set(count.values())!={1}:
        return False
    else:
        return True

def checkRect(arr):
    for i in range(0, 9, 3):
        rows = arr[i:i+3]
        for i in range(0,9,3):
            temp = []
            for row in rows:
                temp.append(row[i:i+3])
            temp = sum(temp,[])
            # print("==============",temp)
            if not checkCount(temp):
                return False
    return True

T  = int(input())
for idx in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    if checkRow(arr) and checkCol(arr) and checkRect(arr):
        print('#{0} 1'.format(idx+1))
    else:
        print('#{0} 0'.format(idx+1))

        