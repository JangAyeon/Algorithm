import sys
n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())
search = list(map(int,input().split()))

def binary_search(arr, target, start, end):
    if start>end:
        return 0 # 존재하지 않음
        
    mid = (start + end)//2
    
    # 찾은 경우 해당 mid 앞뒤로 중복 원소 있는지 확인 필요
    if arr[mid] == target:
        i, j = 1, 1
        
        # mid에서 한 칸씩 앞으로
        while mid - i>=start:
            #print("---전진확인---")
            #print(target,i,j)
            #print(arr[mid-i], arr[mid])
            #print("---전진확인 끝---")
            
            if arr[mid-i]!=arr[mid]: # 앞에 다른 수임 더이상 확인 필요 X
                #print("전진 끝")
                break
            else: 
                i+=1
        # mid에서 한 칸씩 뒤로
        while mid+j<=end:
            #print("---후진확인---")
            #print(target,i,j)
            #print(arr[mid+j], arr[mid])
            #print("---후진확인 끝---")
            
            if arr[mid+j]!=arr[mid]: # 뒤에 다른 수임 더이상 확인 필요 X
                #print("후진 끝")
                break
            else:
                j+=1
        
        return i+j-1
            
        
    # 중간점의 값보다 찾는 값이 작은 경우 왼쪽 확인 필요
    elif arr[mid]>target: # 줄여야함
        return binary_search(arr, target, start, mid-1)
    # 중간점의 값보다 찾는 값이 큰 경우 오른쪽 확인 필요
    else: # 키워야 함
        return binary_search(arr, target,mid+1, end)


n_dic = {}
for target in search:
    start = 0
    end = len(arr) - 1
    if target not in n_dic:
        n_dic[target] = binary_search(arr, target, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in search ))
    

        
        
