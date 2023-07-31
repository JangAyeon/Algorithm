SHEEP = 0
WOLF = 1

def create_nextNodes(idx, node, nodes, edge_list):
    # 노드 리스트에서 현재 인덱스의 노드 제외 + 현재 노드의 자식 노드 
    #print("idx",idx)
    #print("node", node)
    #print(edge_list[node])
    return nodes[:idx] +  nodes[idx+1:]+edge_list[node]

def create_parent2child(info, edges):
    edge_list = [[] for _ in range(len(info))]
    for parent, child in edges:
        edge_list[parent].append(child)
    return edge_list

def search(nodes, edge_list, info, sheep, wolf):
    if not nodes: # 더이상 탐색 없음
        return sheep
    max_sheep = sheep
    for idx, node in enumerate(nodes):
        new_next_nodes = create_nextNodes(idx, node, nodes, edge_list)
        if info[node] == SHEEP:
            max_sheep =max(search(new_next_nodes, edge_list, info, sheep+1, wolf), max_sheep)
        elif sheep>wolf+1:
            max_sheep =max(search(new_next_nodes, edge_list, info, sheep, wolf+1),max_sheep)
    return max_sheep
        

def solution(info, edges):
    edge_list = create_parent2child(info, edges)
    #print(len(edge_list))
    answer = search([0], edge_list, info, 0, 0)
    return answer

#info  =[0,0,1,1,1,0,1,0,1,0,1,1]
#edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

#solution(info, edges)
    