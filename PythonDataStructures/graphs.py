
# Edge List: [[from, to], [from, to], [n , n]]
# Adjacency List: (hashmap) {nodes value: array of all nodes we can travel to}

v = 8 
a = [[0,1], [1, 2], [0,3], [3,4], [3,6], [3, 7], [4, 2], [4, 5], [5,2]]


# Convert edge list to adjacency list
from collections import defaultdict
from importlib.machinery import NamespaceLoader
D = defaultdict(list)
for u, v in a:
    D[u].append(v)

print(D)

# DFS time complexity: O(V + E)
def dfs_recursive(node):
    print(node)
    for neighbor in D[node]:
        if neighbor not in seen_set:
            seen_set.add(neighbor)
            dfs_recursive(neighbor)

begin = 0
seen_set = set()
seen_set.add(begin)
dfs_recursive(begin) 




# iterative dfs
begin = 0
seen_set = set()
seen_set.add(begin)
stack = [begin]

while stack:
    node = stack.pop()
    print(node)
    for neighbor in D[node]:
        if neighbor not in seen_set:
            seen_set.add(neighbor)
            stack.append(neighbor)


            # iterative BFS
from collections import deque
# BFS time complexity: O(V + E)
source = 0 
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for neighbors in D[node]:
        if neighbors not in seen:
            seen.add(neighbors)
            q.append(neighbors) 


# Does a path exist from a specific node to another for a directed graph?
def hasPath(graph, src, dest):
    if src == dest:
        return True
    for nei in graph[src]:
        if hasPath(graph, nei, dest):
            return True
    return False


# Does a path exist from a specific nodd to another with for an undirected graph?

def hashPathUndirected(edges, source, destination):
    adjacency_list = {}
    for u, v in edges:
        if u not in adjacency_list:
            adjacency_list[u] = []
        if v not in adjacency_list:
            adjacency_list[v] = []
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)


    stk = [source]
    visited = set(source)
    while stk:
        node = stk.pop()
        if node == destination:
            return True
        for nei in adjacency_list[node]:
            if nei not in visited:
                visited.add(nei)
                stk.append(nei)
    return False

# count the number of components in an undirected graph 

def returnComponentCount(graph):
    components = 0 
    stk = []
    visited = set()
    
    for node in graph:
        if node not in visited:
            visited.add(node)
            stk.append(node)
            components += 1

        while stk:
            curr = stk.pop()
            for nei in graph[curr]:
                if nei not in visited:
                    visited.add(nei)
                    stk.append(nei)
        
    return components


def shortestPathUndirected(graph, start, end):

    if start == end:
        return 0

    q = deque([(start, 0)])
    visited = set([start])

    while q:
        node, distance = q.popleft()
        for nei in graph[node]:
            if nei == end:
                return distance + 1
            if nei not in visited:
                visited.add(nei)
                q.append((nei, distance + 1))
            
    return -1


def dijkstraShortestPath():
    # visited set 
    # we need a table to sore, node, shortest distance, and previous node