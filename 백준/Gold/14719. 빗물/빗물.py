import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

#print(n,m,arr)

def countBlock(arr):
    count  = 0
    
    idx = 0
    start = arr[idx]
    stack = []
    step = 0

    while idx <len(arr):
        #print(stack)
        if start < arr[idx]:
            count +=stack[0]*len(stack) - sum(stack)
            #print(count)
            stack = []
            step = 0
            start = arr[idx]
    
        stack.append(arr[idx])
        idx+=1
    if len(stack)>1 and stack[0]<=stack[-1]:
        count +=stack[0]*len(stack) - sum(stack)
    return count,stack
  
temp1=temp2=0 
stack1=[]
stack2=[]
temp1, stack1 =countBlock(arr)
if len(stack1)>1:
    temp2, stack2 =countBlock(list(reversed(stack1)))
 
    
print(temp1+temp2)