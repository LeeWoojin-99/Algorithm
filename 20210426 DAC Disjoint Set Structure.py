'''
2021. 04. 26.
Daily Algorithm Coding
disjoint set structure realization algorithm
'''
import heapq

#disjoint set structure realization algorithm code
def DSS_find(parent, x):
	if parent[x] != x:
		parent[x] = DSS_find(parent, parent[x])
	return parent[x]

def DSS_union(parent, x, y):
	x = DSS_find(parent, x)
	y = DSS_find(parent, y)

	if x > y:
		parent[x] = y
	else:
		parent[y] = x

node, edge = map(int, input().split())
parent = [0]*(node+1)
edge_data = []

for i in range(node+1):
	parent[i] = i

for _ in range(edge):
	x, y = map(int, input().split())
	edge_data.append((x, y))

for x, y in edge_data:
	DSS_union(parent, x, y)

print("\ndisjoint set structure realization")
for i in range(1, node+1):
	DSS_find(parent, i)
	print(parent[i], end=' ')
print()


#kruskal's algorithm code
node, edge = map(int, input().split())
parent = [0]*(node+1)
edge_data = []
distance_sum = 0

for i in range(node+1):
	parent[i] = i

for _ in range(edge):
	x, y, dist = map(int, input().split())
	heapq.heappush(edge_data, (dist, x, y))

while edge_data:
	dist, x, y = heapq.heappop(edge_data)

	x = DSS_find(parent, x)
	y = DSS_find(parent, y)

	if x != y:
		DSS_union(parent, x, y)
		distance_sum += dist

print("minimum spanning tree")
print(distance_sum)

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