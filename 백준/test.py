def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b,truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in truth and b in truth:
        return

    if a in truth:
        parent[b] = a
    
    elif b in truth:
        parent[a] = b
    
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    #print(a, b)
    #print(truth, parent)


def sol():
    N, M = map(int, input().split())
    truth = list(map(int, input().split()))[1:]


    # 진실을 아는 집합은 루트 노드가 0인 집합으로 표시
    parent = list(range(N+1))

    parties = []
    for _ in range(M):
        party = list(map(int, input().split()))[1:]
        # 같은 파티의 사람들을 모두 같은 집합으로 합침
        for i in range(len(party) - 1):
            union(parent, party[i], party[i+1], truth)
        parties.append(party)

    cnt = 0  # 거짓말을 할 수 있는 파티 수
    for party in parties:
        for p in party:
            if find(parent, p) in truth:
                break
        else:
            cnt += 1
    return cnt
 

print(sol())