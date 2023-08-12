class Node:
    def __init__(self, data, left_data, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회 : VLR
def pre_order(node):
    print(node.data, end=" ") # V
    if node.left_node !=None: # L
        pre_order(tree[node.left_node])
    if node.right_node !=None: # R
        pre_order(tree[node.right_node])

# 중위 순회 : LVR
def in_order(node):
    if node.left_node !=None: # L
        in_order(tree[node.left_node])
    print(node.data, end=" ") # V
    if node.right_node !=None: # R
        in_order(tree[node.right_node])
        
# 후위 순회 : LRV
def post_order(node):
    if node.left_node !=None: # L
        post_order(tree[node.left_node])
    if node.right_node !=None: # R
        post_order(tree[node.right_node])
    print(node.data, end=" ") # V
    
    
n = int(input())
tree={}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node =="None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)
    
pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])