
def create_parent2child(info, edges):
    
    edge_list = [[] for _ in range(len(info))]
    for parent, child in edges:
        edge_list[parent].append(child)
    return edge_list
    
def create_nextNodes(idx,node, nodes, edge_list):
    return nodes[:idx]+nodes[idx+1:]+edge_list[node]

def search(nodes, edge_list, info, sheep, wolf):
    if not(nodes):
        return sheep
    max_sheep = sheep
    for idx, node in enumerate(nodes):
        next_nodes = create_nextNodes(idx,node, nodes, edge_list)
        #print(next_nodes)
        if info[node] == 0:
            max_sheep = max(search(next_nodes, edge_list, info, sheep+1, wolf),max_sheep)
        elif info[node]==1 and sheep>wolf+1:
            max_sheep = max(search(next_nodes, edge_list, info, sheep, wolf+1), max_sheep)
    return max_sheep
            
def solution(info, edges):
    edge_list = create_parent2child(info, edges)
    answer = search([0], edge_list, info, 0, 0)
    return answer
    

