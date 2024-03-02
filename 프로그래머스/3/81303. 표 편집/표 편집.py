class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n,k,cmds):
    nodes = [Node() for _ in range(n)]
    curr = nodes[k]
    stack = []
    answer = []
    for idx in range(1, n):
        nodes[idx-1].next = nodes[idx]
        nodes[idx].prev = nodes[idx-1]

    for cmd in cmds:
        if cmd[0]=="D":
            step = int(cmd[2:])
            for _ in range(step):
                curr = curr.next
        elif cmd[0]=="U":
            step = int(cmd[2:])
            for _ in range(step):
                curr = curr.prev
        elif cmd[0]=="C":
            stack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node
            
                
    
    for i in range(len(nodes)):
        if nodes[i].removed:
            answer.append("X")
        else:
            answer.append("O")
    
    return "".join(answer)




