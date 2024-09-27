# Helper Code
from collections import defaultdict
import sys
class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional 
        
    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)

''' TO DO: Find the shortest path from the source node to every other node in the given graph '''
def dijkstra(graph, source):
    result = {node: sys.maxsize for node in graph.nodes}  # Start with all distances as infinity
    result[source] = 0  # Distance from source to itself is 0
    unvisited = set(graph.nodes)  # All nodes are unvisited initially
    path = {node: None for node in graph.nodes}  # Tracks the best previous node

    # Step 2: Loop until all nodes have been visited
    while unvisited:
        # Find the unvisited node with the smallest known distance
        current_node = find_min_node(unvisited, result)
        
        # If current_node is still infinity, we break the loop as remaining nodes are disconnected
        if result[current_node] == sys.maxsize:
            break
        
        # Step 3: Explore the neighbors of the current node
        for neighbour in graph.neighbours[current_node]:
            if neighbour in unvisited:  # Only consider unvisited neighbours
                # Calculate the new tentative distance to this neighbor
                new_distance = result[current_node] + graph.distances[(current_node, neighbour)]
                
                # If a shorter path is found, update the distance and path
                if new_distance < result[neighbour]:
                    result[neighbour] = new_distance
                    path[neighbour] = current_node  # Update the optimal path

        # Step 5: Remove the current node from the unvisited set
        unvisited.remove(current_node)
        # 1. Find the unvisited node having smallest known distance from the source node.
        
        # 2. For the current node, find all the unvisited neighbours. For this, you have calculate the distance of each unvisited neighbour.
        
        # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary, update the shortest distance in the result dictionary.        

        # 4. If there is an update in the result dictionary, you need to update the path dictionary as well for the same key.
                    
        # 5. Remove the current node from the unvisited set.

    return result
    
def find_min_node(unvisited, result):
    min_distance = float('inf')  # Start with an infinite distance
    min_node = None
    
    for node in unvisited:
        # We are looking for the node with the smallest distance in result.
        if result[node] < min_distance:
            min_distance = result[node]
            min_node = node
    
    return min_node

# Test 1
testGraph = Graph()
for node in ['A', 'B', 'C', 'D', 'E']:
    testGraph.add_node(node)

testGraph.add_edge('A','B',3)
testGraph.add_edge('A','D',2)
testGraph.add_edge('B','D',4)
testGraph.add_edge('B','E',6)
testGraph.add_edge('B','C',1)
testGraph.add_edge('C','E',2)
testGraph.add_edge('E','D',1)

print(dijkstra(testGraph, 'A'))     # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

# Test 2
graph = Graph()
for node in ['A', 'B', 'C']:
    graph.add_node(node)
    
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 5)
graph.add_edge('A', 'C', 10)

print(dijkstra(graph, 'A'))        # {'A': 0, 'C': 10, 'B': 5}

# Test 3
graph = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F']:
    graph.add_node(node)
    
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 4)
graph.add_edge('D', 'C', 1)
graph.add_edge('B', 'C', 2)
graph.add_edge('A', 'D', 2)
graph.add_edge('B', 'F', 2)
graph.add_edge('C', 'F', 3)
graph.add_edge('E', 'F', 2)
graph.add_edge('C', 'E', 1)

print(dijkstra(graph, 'A'))# {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}