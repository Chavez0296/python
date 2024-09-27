from queue import Queue
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []
    def __str__(self) -> str:
        return f"{self.value}"    
    def add_child(self,new_node):
        self.children.append(new_node)
    
    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list

    def display(self):
        return f"{self.nodes}"

    def __str__(self):
        return f"{self.nodes}"    
        
    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)
            
    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA])

graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

#placeholder = []
#for x in range(len(graph1.nodes)):
#    placeholder.append(graph1.nodes[x].value)
#    placeholder.append(':')
#    for z in range(len(graph1.nodes[x].children)):
#        print(graph1.nodes[x].children[z])
#        placeholder.append(str(graph1.nodes[x].children[z]))
#    placeholder.append(' -- ')
#print(placeholder)
#graph1.display()

def bfs_search(root_node, search_value):
    visited = {}
    parent = {}
    node = root_node.value
    target = search_value
    frontier = Queue()
    
    frontier.put(root_node)
    visited[node] = 'Black'
    parent[node] = node
    #print(visited)
    while not frontier.empty():
        s = frontier.get()
        if(target == s.value):
            return s
        for v in s.children:
            if v.value not in visited:
                visited[v.value] = 'Black'
                parent[v.value] = s.value   
                frontier.put(v)
        #print(visited)

   # print(visited)
   # print(parent)

assert nodeA == bfs_search(nodeS, 'A')
assert nodeS == bfs_search(nodeP, 'S')
assert nodeR == bfs_search(nodeH, 'R')

print(nodeA == bfs_search(nodeS, 'A'))
print(nodeS == bfs_search(nodeP, 'S'))
print(nodeR == bfs_search(nodeH, 'R'))
print(nodeS == bfs_search(nodeP, 'F'))
