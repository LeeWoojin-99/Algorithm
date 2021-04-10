'''
2021. 04. 10
daily algorithm coding
disjoint sets structure realization algorithm
structure : 자료구조
realization : 실현, 구현, 현실화, 달성
서로소 집합 자료구조 계산 알고리즘
kruskal's algorithm
크러스컬 알고리즘
'''

#disjoint sets structure realization algorithm
def find_parent(parent, find_x):
	if find_x != parent[find_x]:
		parent[find_x] = find_parent(parent, parent[find_x])
	return parent[find_x]

def union_parent(parent, union_x, union_y):
	union_x = find_parent(parent, union_x)
	union_y = find_parent(parent, union_y)
	if union_x < union_y:
		parent[union_y] = union_x
	else:
		parent[union_x] = union_y

n_node, n_edge = map(int, input().split())
parent = [0]*(n_node+1)

for i in range(n_node+1):
	parent[i] = i

for i in range(n_edge):
	a, b = map(int, input().split())
	union_parent(parent, a, b)

print("\nroot node : ", end='')
for i in range(1, n_node+1):
	print(parent[i], end=' ')

print("\nfind_parent : ", end='')
for i in range(1, n_node+1):
	print(find_parent(parent, i), end=' ')

print("\nroot node : ", end='')
for i in range(1, n_node+1):
	print(parent[i], end=' ')

'''
6 4
1 4
2 3
2 4
5 6
node edge
edge data
edge data : start node, end node
'''


#kruskal's algorithm
#서로소 집합 자료구조를 이용하여 최소 신장 트리를 만드는 알고리즘

n_node, n_edge = map(int, input().split())
parent = [0]*(n_node+1)
distance = []
result = 0

for i in range(n_node+1):
	parent[i] = i

for i in range(n_edge):
	x, y, cost = map(int, input().split())
	distance.append((cost, x, y))

distance.sort()

for i in distance:
	cost, a, b = i
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a != b:
		#둘이 다르면 사이클이 발생하지 않는다는 의미
		union_parent(parent, a, b)
		result += cost

print()
print(result)

'''
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