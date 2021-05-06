'''
2021. 05. 06.
Daily Algorithm Coding
1. Disjoint Set Structure Realization Algorithm
2. Kruskal's Algorithm
'''

import heapq

def dss_find(parent, x):
	if parent[x] != x:
		parent[x] = dss_find(parent, parent[x])
	return parent[x]

def dss_union(parent, x, y):
	x = parent[x]
	y = parent[y]
	if x > y:
		parent[x] = y
	else:
		parent[y] = x


# disjoint set structure realization algorithm code
n, e = map(int, input().split())
parent = [[] for _ in range(n+1)]

for i in range(n+1): parent[i] = i

for i in range(e):
	x, y = map(int, input().split())
	dss_union(parent, x, y)

print("\ndisjoint set structure : ", end='')
for i in range(1, n+1):
	dss_find(parent, i)
	print(parent[i], end=' ')
print()


# kruskal's algorithm
n, e = map(int, input().split())
parent = [[] for _ in range(n+1)]
q = []
result = 0

for i in range(n+1): parent[i] = i

for i in range(e):
	x, y, dist = map(int, input().split())
	heapq.heappush(q, (dist, x, y))

while q:
	dist, x, y = heapq.heappop(q)
	if dss_find(parent, x) != dss_find(parent, y):
		dss_union(parent, x, y)
		result += dist

print("kruskal algorithm : %d"%result)



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
'''