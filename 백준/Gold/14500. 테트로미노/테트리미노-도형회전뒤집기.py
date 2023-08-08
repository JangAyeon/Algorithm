import sys
input = sys.stdin.readline

row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(row)]
#print(row, col, graph)

shapes = [
     [[1,1],[1,1]], # 네모
     [[1,1,1,1]], # | 가로길쭉 
     [[1,1,1],[0,1,0]], # T모양
     [[1,0],[1,1],[0,1]], # 꺽은 S자
     [[1,0],[1,0],[1,1]] # L모양
]


def get_shape(k, curr_shape):
    if k == 0: return shapes[0]
    elif k == 1:return shapes[1]
    elif k == 3: return shapes[2]
    elif k == 7: return shapes[3]
    elif k == 11: return shapes[4]
    elif k in [9, 15]: return flip(curr_shape)
    else: return rotate(curr_shape)
    
def get_score(shape,i,j,graph):
    height, width = len(shape), len(shape[0])
    score = 0
    for r in range(height):
        for c in range(width):
            #print(i,j,r,c)
            score+=shape[r][c] * graph[i+r][j+c]
    #print(shape,score)
    return score
    
def get_max(shape, r, c, graph):
    height, width = len(shape), len(shape[0])
    max_score = 0
    for i in range(r - height+1):
        for j in range(c-width+1):
            max_score = max(max_score , get_score(shape, i, j, graph))
    #print(max_score)
    return max_score
    
def flip(shape):
    height, width = len(shape), len(shape[0])
    curr_shape = [[0]*width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            curr_shape[i][j] = shape[i][width-j-1]
    #print("flip", curr_shape, shape)
    return curr_shape
    
def rotate(shape):
    height, width = len(shape[0]), len(shape)
    curr_shape =  [[0]*width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            #print(i,j)
            #print(width-j-1)
            curr_shape[i][j] = shape[width-j-1][i]
    #print("rotate", curr_shape, shape)
    return curr_shape
    
def solution(r, c, graph):
    
    answer = 0
    shape = []
    for k in range(19):
        shape = get_shape(k, shape)
        answer = max(answer, get_max(shape, r, c, graph))
    
    return answer
    
print(solution(row, col, graph))
