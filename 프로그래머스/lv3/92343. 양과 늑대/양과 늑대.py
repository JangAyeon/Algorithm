def create_edge_list(info, edges):
    edge_list = [[] for _ in range(len(info))]
    for parent, child in edges:
        edge_list[parent].append(child)
    return edge_list
    
def create_node_list(idx,node, nodes, edge_list):
    return nodes[:idx]+nodes[idx+1:]+edge_list[node]
    
def search(nodes, edge_list, info, sheep, wolf):
    if not(nodes): # 더이상 노드 없는 경우
        return sheep
    
    max_sheep = sheep
    for idx, node in enumerate(nodes):
        new_nodes = create_node_list(idx ,node, nodes ,edge_list)
        #print(new_nodes)
        if info[node]==0:
            max_sheep =  max(max_sheep,search(new_nodes, edge_list, info, sheep+1, wolf))
        elif info[node]==1 and sheep>wolf+1:
            max_sheep = max(max_sheep, search(new_nodes, edge_list, info, sheep, wolf+1))
    return max_sheep


def solution(info, edges):
    edge_list = create_edge_list(info, edges)
    answer = search([0], edge_list,info,  0, 0)
    return answer

