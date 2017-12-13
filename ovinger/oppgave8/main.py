from sys import stdin
class Node:
    def __init__(self):
        self.child = []
        self.ratatosk = False
        self.next_child = 0
def bfs(root):
    explored = []
    queue = []
    queue.append(root)
    queue.append(None)
    depth = 0
    while queue:
        node = queue.pop(0)
        if node == None:
            depth += 1
            queue.append(None)
            continue
        if node.ratatosk:
            return depth
        if node not in explored:
            explored.append(node)
            neighbours = node.child
            for neighbour in neighbours:
                queue.append(neighbour)
function = stdin.readline().strip()
number_of_nodes = int(stdin.readline())
nodes = []
for i in range(number_of_nodes):
    nodes.append(Node())
start_node = nodes[int(stdin.readline())]
ratatosk_node = nodes[int(stdin.readline())]
ratatosk_node.ratatosk = True
for line in stdin:
    number = line.split()
    temp_node = nodes[int(number.pop(0))]
    for child_number in number:
        temp_node.child.append(nodes[int(child_number)])
print(bfs(start_node))
