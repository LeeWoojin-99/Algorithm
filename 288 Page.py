'''
288 Page
크루스칼 알고리즘
최소 신장 트리를 만드는데 필요한 비용을 계산하는 알고리즘
'''
'''
비용이 적은 간선부터 확인하면서
사이클이 발생하지 않으면 신장 트리 간선에 추가,
발생한다면 추가하지 않는 과정을
모든 간선에 대하여 수행한다.
'''

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a<b:
		parent[b] = a
	else:
		parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)

edges = []
result = 0

for i in range(1, v+1):
	parent[i] = i

for _ in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()

for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

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
'''