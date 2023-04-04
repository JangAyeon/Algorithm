import sys
#from collections import defaultdict
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def isGigaIsRoot(tree, root):
    nodes = []
    for i in range(len(tree)):
        nodes+=list(tree[i].keys())

    if root not in nodes:
        return True
    else:
        return False

def get_maxbranch(tree, root):
    if isGigaIsRoot(tree, root):
        return 0

    maxbranch = 0
    for node, w in tree[root].items():
        del tree[node][root]
        branch = w + get_maxbranch(tree, node)
        if branch > maxbranch :
            maxbranch = branch
    return maxbranch

# 변수초기화
n, r= map(int, input().split())
tree = [{} for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree[a][b] = w
    tree[b][a] = w

# 기가노드까지의 기둥 길이 찾기
def findGiga(root, distance):
    while len(tree[root])==1:
        node, weight = list(tree[root].items())[0]
        del tree[node][root]
        distance += weight
        root = node
    return root, distance


gigaNode, gigaDistance = findGiga(r, 0)
maxbranch = get_maxbranch(tree, gigaNode)

print('{} {}'.format(gigaDistance, maxbranch))