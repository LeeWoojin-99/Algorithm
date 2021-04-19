'''
2021. 04. 19.
Daily Algorithm Coding
Graph Algorithms
1. disjoint set structure realization algorithm
2. kruscal's algorithm
3. topology algorithm
'''
from collections import deque

#disjoint set structure realization algorithm code
def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]

def parent_union(parent, x, y):
    x = parent_find(parent, x)
    y = parent_find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, e = map(int, input().split())
parent = [0]*(n+1)

for i in range(n+1):
    parent[i] = i

for i in range(e):
    x, y = map(int, input().split())
    parent_union(parent, x, y)

print("disjoint set structure")
for i in range(1, n+1):
    parent_find(parent, i)
    print(parent[i], end=' ')
print()


#kruskal's algorithm code
print("kruskal algorithm")
n, e = map(int, input().split())
parent = [0]*(n+1)
distance = []
min_distance = 0

for i in range(n+1):
    parent[i] = i

for i in range(e):
    x, y, dist = map(int, input().split())
    distance.append((dist, x, y))

distance.sort()

for i in range(e):
    dist, x, y = distance[i]
    x = parent_find(parent, x)
    y = parent_find(parent, y)

    if x != y:
        parent_union(parent, x, y)
        min_distance += dist

print(min_distance)


#topology sort algorithm code
print("topology sort")
n, e = map(int, input().split())
graph = [[] for i in range(n+1)]
indegree = [0]*(n+1)

for i in range(e):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ')

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            queue.append(i)


''' disjoint set structure realization algorithm input data
6 4
1 4
2 3
2 4
5 6
node edge
edge data : start node, end node
'''
''' kruskal's algorithm input data
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
node edge
edge data
edge data : start node, end node, distance
'''
''' topology sort algorithm input data
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
node edge
edge data
edge data : start node, end node
'''
'''
6 4
1 4
2 3
2 4
5 6
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''