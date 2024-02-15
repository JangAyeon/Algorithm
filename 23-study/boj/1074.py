import sys
input = sys.stdin.readline

# 0-indexing
n,r,c = map(int, input().split())

# 배열을 크기가 2N-1 × 2N-1로 4등분 한 후
def area(n,r,c):
    size = 2**(n-1)
    
    if r<size and c<size:
        
        #print(0)
        return 0
    elif r<size and c>=size:
        #print(1)
        return 1
    elif r>=size and c<size:
        #print(2)
        return 2
    else:
        #print(3)
        return 3
        

def visit(n,r,c):
    if n==1:
        return area(n,r,c)
    size = 2**(n-1)
    q = area(n,r,c)
    visited = size*size*q
    #print(visited, q)
    if q==0:
        return visited + visit(n-1,r,c)
    elif q==1:
        return visited + visit(n-1,r, c-size)
    elif q==2:
        return visited + visit(n-1, r-size, c)
    else:
        return visited + visit(n-1, r-size, c-size)
        
print(visit(n,r,c))
    