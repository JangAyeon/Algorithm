import sys
n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
search = list(map(int,input().split()))
s_search = sorted(search)

start, end = 0, len(arr)-1
answer = [0 for _ in range(len(search))]

while s_search:
    num = s_search.pop(0)
    idx = search.index(num)
    start, end = 0, len(arr)-1
    while start<=end:
        mid = (start+end)//2
        #print("========")
        #print(start, mid, end)
        #print(arr[mid], num)
        #print("========")
        if arr[mid] == num:
            answer[idx]=1
            #print("find")
            break
        elif arr[mid]>num: # 줄여야 함
            end = mid-1
        else:
            start = mid+1
            
    #print(num,idx, answer, search, s_search)

#print(n,m,arr, search)

for i in answer:
    print(i)