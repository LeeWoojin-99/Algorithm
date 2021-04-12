'''
2021. 04. 12.
Daily Algorithm Coding
1. disjoint sets structure realization algorithm
2. kruskal's algorithm
3. topology sort algorithm
'''
from collections import deque

#disjoint sets structure realization algorithm code
def DSS_find(parent, x):
	#DSS : Disjoint Sets Structure
	if parent[x] != x:
		parent[x] = DSS_find(parent, parent[x])
	return parent[x]

def DSS_union(parent, x, y):
	x = DSS_find(parent, x)
	y = DSS_find(parent, y)
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
	DSS_union(parent, x, y)

print("disjoint sets structure realizaiton algorithm")
for i in range(1, n+1):
	DSS_find(parent, i)
	print(parent[i], end=' ')
print()


#kruskal's algorithm
n, e = map(int, input().split())
parent = [0]*(n+1)
edge_data = []
sum_distance = 0

for i in range(n+1):
	parent[i] = i

for i in range(e):
	x, y, dist = map(int, input().split())
	edge_data.append((dist, x, y))

edge_data.sort()

for i in edge_data:
	dist, x, y = i
	x = DSS_find(parent, x)
	y = DSS_find(parent, y)
	if x != y:
		DSS_union(parent, x, y)
		sum_distance += dist

print("kruskal algorithm")
print(sum_distance)


#topology sort algorithm
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

print("topology sort algorithm")
while queue:
	x = queue.popleft()
	print(x, end=' ')
	for i in graph[x]:
		indegree[i] -= 1
		if indegree[i] == 0:
			queue.append(i)


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