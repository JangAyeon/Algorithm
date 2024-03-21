N, Q = map(int, input().split())
N = 2**N        # N크기 저장
arr = [[0]*(N+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(N+2)]
lst = list(map(int, input().split()))
for L in lst:   # Q번 시전할 부분격자 크기 순차처리
    L = 2**L    # (부분격자) 한 변 크기 저장

    # [1] 부분격자를 시계방향 90도 회전
    new = [[0]*(N+2) for _ in range(N+2)]
    for si in range(1, N+1, L):
        for sj in range(1, N+1, L):   # 가능한 모든 기준위치(좌측상단)
            for i in range(L):
                for j in range(L):
                    new[si+i][sj+j]=arr[si+L-1-j][sj+i]
    arr = new
    print("회전")
    for i in arr:
        print(*i)
    print("======")
    # [2] 네방향, 0이 2개 이상이면 얼음 -감소
    new = [x[:] for x in arr]           # arr을 deepcopy
    melts = []
    for i in range(1, N+1):
        for j in range(1, N+1):         # 전체를 순회
            if arr[i][j]==0:    continue# 얼음 아니면 skip..

            cnt=0
            for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
                if arr[i+di][j+dj]!=0:  # 얼음이 아니면
                    cnt+=1
            if cnt>=2 and arr[i][j]!=0:
                melts.append([i,j])
            print(i,j,arr[i+di][j+dj], i+di, j+dj)

    for r,c in melts:
        arr[r][c]-=1

    arr=new

    for i in arr:
        print(*i)

def bfs(si,sj):
    q = []              # [0] q, v[], 정답관련 변수등 생성

    q.append((si,sj))   # [1] q에 초기데이터(들)삽입, v[], ..
    v[si][sj]=1
    cnt=1

    while q:
        ci,cj = q.pop(0)
        # 네방향, 미방문, **조건:얼음이면(>0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni,nj = ci+di, cj+dj
            if v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

# [3] 정답처리: 남은 얼음덩어리중 가장 큰 크기
v = [[0]*(N+2) for _ in range(N+2)]
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if v[i][j]==0 and arr[i][j]>0:  # 미방문 얼음이면
            ans = max(ans, bfs(i,j))
print(sum(map(sum,arr)))
print(ans)