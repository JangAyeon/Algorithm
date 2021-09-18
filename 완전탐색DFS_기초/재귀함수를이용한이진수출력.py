#code before lecture

n=int(input())
res=""

while(n!=0):
    n,r=divmod(n,2) #몫과 나머지 반환
    res+=str(r)
    
print(int(res[::-1]))

#code from lecture
def DFS(x):
    if x==0:
        return;
    else:
        DFS(x//2)
        print(x%2,end=" ")


if__name__=="__main__":
    n=int(input())
    DSF(n)


#code after lecture

def DFS(n):
    if n!=0:
        a,b=divmod(n,2)
        DFS(a)
        print(b,end="")

n=int(input())
DFS(n)
