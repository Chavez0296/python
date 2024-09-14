
'''
        A
       / \
      B<- C
     / \   \
    D   E ->F
   /
  G
 /
H
'''

adj_list = {
    "A": ["B", "C"],
    "B": ["D","E"],
    "C": ["B", "F"],
    "D": ["G","H"],
    "E": ["F"],
    "F": [],
    "G": ["H"],
    "H": []
}

color = {} #W, G, B
parent = {}
trav_time = {} #[start,end]
dfs_traversal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1,-1]
print(color)
print()
print(parent)
print()
print(trav_time)

time = 0
def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1
    
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)
    
    color[u] = "B"
    trav_time[u][1]= time
    time +=1
print()
dfs_util("A")
print(dfs_traversal_output)
print(parent)
print(trav_time)