class Node:
    def __init__(self, data, left_data, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회 : VLR
def pre_order(node):
    print(node.data, end="") # V
    if node.left_node !=".": # L
        pre_order(tree[node.left_node])
    if node.right_node !=".": # R
        pre_order(tree[node.right_node])

# 중위 순회 : LVR
def in_order(node):
    if node.left_node !=".": # L
        in_order(tree[node.left_node])
    print(node.data, end="") # V
    if node.right_node !=".": # R
        in_order(tree[node.right_node])
        
# 후위 순회 : LRV
def post_order(node):
    if node.left_node !=".": # L
        post_order(tree[node.left_node])
    if node.right_node !=".": # R
        post_order(tree[node.right_node])
    print(node.data, end="") # V
    
    
n = int(input())
tree={}

for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])