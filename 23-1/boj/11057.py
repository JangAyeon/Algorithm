import sys
input = sys.stdin.readline

N=int(input().strip()) 

temp = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


for row in range(1, N+1):
    array = []
    for col in range(0, len(temp[row-1])):
        #print("row - 1 : ",row-1,temp[row-1])
        #print("row : ",row,temp[row])
        a = sum(temp[row-1][:col+1])
        array.append(a)
        #print(temp[col], col, a )
    temp.append(array)
        #temp[row][col] = a
        #temp[row][col] = sum(temp[row-1][:col+1])
#print(temp)
print(temp[N][-1]% 10007)