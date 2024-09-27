# Helper Class
class GraphEdge(object):
    def __init__(self, destinationNode, distance):
        self.node = destinationNode
        self.distance = distance

# Helper Classes
class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.edges = []

    def add_child(self, node, distance):
        self.edges.append(GraphEdge(node, distance))

    def remove_child(self, del_node):
        if del_node in self.edges:
            self.edges.remove(del_node)

class Graph(object):
    def __init__(self, node_list):
        self.nodes = node_list

    # adds an edge between node1 and node2 in both directions
    def add_edge(self, node1, node2, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2, distance)
            node2.add_child(node1, distance)

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

import math
import heapq

def dijkstra(graph, start_node, end_node):
    result = {node: math.inf for node in graph.nodes}
    result[start_node] = 0
    pq = [(0, start_node.value, start_node)]  
    visited = set()

    while pq:
    
        current_dist, cd, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end_node:
            return current_dist

        for edge in current_node.edges:
            neighbour = edge.node
            distance = edge.distance

            if neighbour not in visited:
                new_distance = current_dist + distance

                if new_distance < result[neighbour]:
                    result[neighbour] = new_distance
                    heapq.heappush(pq, (new_distance, neighbour.value, neighbour))

    return result
    

# Test Case 1:

# Create a graph
node_u = GraphNode('U')
node_d = GraphNode('D')
node_a = GraphNode('A')
node_c = GraphNode('C')
node_i = GraphNode('I')
node_t = GraphNode('T')
node_y = GraphNode('Y')

graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])

# add_edge() function will add an edge between node1 and node2 in both directions
graph.add_edge(node_u, node_a, 4)
graph.add_edge(node_u, node_c, 6)
graph.add_edge(node_u, node_d, 3)
graph.add_edge(node_d, node_c, 4)
graph.add_edge(node_a, node_i, 7)
graph.add_edge(node_c, node_i, 4)
graph.add_edge(node_c, node_t, 5)
graph.add_edge(node_i, node_y, 4)
graph.add_edge(node_t, node_y, 5)

# Shortest Distance from U to Y is 14
print('Shortest Distance from {} to {} is {}'.format(node_u.value, node_y.value, dijkstra(graph, node_u, node_y)))

# Test Case 2
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')

graph = Graph([node_A, node_B, node_C])

graph.add_edge(node_A, node_B, 5)
graph.add_edge(node_B, node_C, 5)
graph.add_edge(node_A, node_C, 10)

# Shortest Distance from A to C is 10
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))

# Test Case 3
node_A = GraphNode('A')
node_B = GraphNode('B')
node_C = GraphNode('C')
node_D = GraphNode('D')
node_E = GraphNode('E')

graph = Graph([node_A, node_B, node_C, node_D, node_E])

graph.add_edge(node_A, node_B, 3)
graph.add_edge(node_A, node_D, 2)
graph.add_edge(node_B, node_D, 4)
graph.add_edge(node_B, node_E, 6)
graph.add_edge(node_B, node_C, 1)
graph.add_edge(node_C, node_E, 2)
graph.add_edge(node_E, node_D, 1)

# Shortest Distance from A to C is 4
print('Shortest Distance from {} to {} is {}'.format(node_A.value, node_C.value, dijkstra(graph, node_A, node_C)))