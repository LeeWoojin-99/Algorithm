'''
2021. 04. 11.
Daily Algorithm Coding
1. disjoint sets structure realization algorithm
2. kruskal's algorithm
3. topology sort algorithm
'''
from collections import deque

#disjoint sets structure realization algorithm code
def ds_find(parent, x):
	if parent[x] != x:
		parent[x] = ds_find(parent, parent[x])
	return parent[x]

def ds_union(parent, x, y):
	x = ds_find(parent, x)
	y = ds_find(parent, y)
	if x < y:
		parent[y] = x
	else:
		parent[x] = y

node, edge = map(int, input().split())
parent = [0]*(node+1)

for i in range(node+1):
	parent[i] = i

for i in range(edge):
	x, y = map(int, input().split())
	ds_union(parent, x, y)

print("\ndisjoint sets structure realization algorithm")
print("parent node : ", end='')
for i in range(1, node+1):
	ds_find(parent, i)
	print(parent[i], end=' ')
print("\n")


#kruskal's algorithm code
print("kruskal algorithm")
node, edge = map(int, input().split())
parent = [0]*(node+1)
edge_data = []
result = 0

for i in range(node+1):
	parent[i] = i

for i in range(edge):
	x, y, dist = map(int, input().split())
	edge_data.append((dist, x, y))

edge_data.sort()

for i in edge_data:
	dist, x, y = i
	x = ds_find(parent, x)
	y = ds_find(parent, y)
	if x != y:
		ds_union(parent, x, y)
		result += dist
print("sum of minimum spanning tree distance : %d"%result)


#topology sort algorithm code
print("\ntopology algorithm")
node, edge = map(int, input().split())
result = []
graph = [[] for i in range(node+1)]
indegree = [0]*(node+1)

for i in range(edge):
	x, y = map(int, input().split())

	graph[x].append(y)
	indegree[y] += 1

queue = deque()
for i in range(1, node+1):
	if indegree[i] == 0:
		queue.append(i)

while queue:
	x = queue.popleft()
	result.append(x)

	for i in graph[x]:
		indegree[i] -= 1
		if indegree[i] == 0:
			queue.append(i)

print("order of visit after using topology sort algorithm : ", end='')
for i in result: print(i, end=' ')


''' disjoint sets structure realization algorithm input data
6 4
1 4
2 3
2 4
5 6
node edge
edge data
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
''' intergrated input data
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