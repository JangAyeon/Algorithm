from collections import Counter
n = int(input())

def getCount(arr):
    count = 0
    if "3" in arr.keys():
        count+=arr["3"]
    if "6" in arr.keys():
        count+=arr["6"]
    if "9" in arr.keys():
        count+=arr["9"]
    #print(count)
    return count

for i in range(1,n+1):
    arr = Counter(list(str(i)))
    count = getCount(arr)
    if count==0:
        print(i, end="")
    else:
        for j in range(count):
            print("-", end="")
    print(" ", end="")


