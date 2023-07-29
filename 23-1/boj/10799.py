import sys
input = sys.stdin.readline
arr = list(input().strip())
stack=[]
l = [] # 레이저
s = []

for idx, i in enumerate(arr):
    if i == ")":
        if stack:
            temp = stack.pop()
            if (idx-temp)==1: # 레이저인 경우
                l.append([temp, idx])
            else:
                s.append([temp, idx]) # 스틱인 경우 
    else:
        stack.append(idx)
            

#print(l)
#print(s)
count = 0
            
for s_s, s_e in s:
    for l_s, l_e in l:
        if s_s<l_s and l_s<s_e: 
            #print(l_s, l_e)
            #print(s_s,s_e)
            #print("=========")
            count+=1
    count+=1
    #print(count)

print(count)