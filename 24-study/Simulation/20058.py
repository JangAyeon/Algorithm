N, Q = map(int, input().split())
N = 2 ** N
##print(N)
arr =[list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))
for L in lst:   # Q번 시전할 부분격자 크기 순차처리
    L = 2**L    # (부분격자) 한 변 크기 저장

    # [1] 부분격자를 시계방향 90도 회전
    new = [[0]*(N) for _ in range(N)]
    for sr in range(0, N, L): # y축
        for sc in range(0, N, L):  # x축 # 가능한 모든 기준위치(좌측상단)
            for r in range(L): # row
                for c in range(L): # col
                    new[sr + c][sc + L - r - 1] = arr[sr + r][sc + c]
    arr = new

    # [2] 네방향, 0이 2개 이상이면 얼음 -감소
    new = [x[:] for x in arr]           # arr을 deepcopy
   #print("회전",N)
    #for i in arr:
    #    print(*i)
    #print("   ====    ")
    melts = []
    for i in range(0, N):
        for j in range(0, N):         # 전체를 순회
            if arr[i][j]==0:    continue# 얼음 아니면 skip..

            cnt=0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                if not(0<=i+di<N) or not(0<=j+dj<N):
                    continue
                if arr[i+di][j+dj]!=0:  # 얼음이면
                    cnt+=1
            if cnt<=2 and arr[i][j]!=0:
                melts.append([i,j])
    #print(melts)

    for r,c in melts:
        new[r][c]-=1

    arr=new

    #for i in arr:
    #    print(*i)

def bfs(si,sj):
    q = []              # [0] q, v[], 정답관련 변수등 생성

    q.append((si,sj))   # [1] q에 초기데이터(들)삽입, v[], ..
    v[si][sj]=1
    cnt=1

    while q:
        ci,cj = q.pop()
        # 네방향, 미방문, **조건:얼음이면(>0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = ci+di, cj+dj
            if not(0<=ni<N) or not(0<=nj<N):
                    continue
            if v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

# [3] 정답처리: 남은 얼음덩어리중 가장 큰 크기
v = [[0]*(N) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if v[i][j]==0 and arr[i][j]>0:  # 미방문 얼음이면
            ans = max(ans, bfs(i,j))
print(sum(map(sum,arr)))
print(ans)