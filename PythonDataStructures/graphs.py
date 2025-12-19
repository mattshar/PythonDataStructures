
# Edge List: [[from, to], [from, to], [n , n]]
# Adjacency List: (hashmap) {nodes value: array of all nodes we can travel to}

v = 8 
a = [[0,1], [1, 2], [0,3], [3,4], [3,6], [3, 7], [4, 2], [4, 5], [5,2]]


# Convert edge list to adjacency list
from collections import defaultdict
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