'''
2021. 06. 07.
Daily Algorithm Coding
Disjoint Sets Structure Realization Algorithm
서로소 집합 자료구조 구현 알고리즘
'''

def find_parent(parent, a):
	# 해당 노드의 최상단 노드(루트 노드)를 찾아주는 함수
	if parent[a] != a:
		parent[a] = find_parent(parent, parent[a])
	return parent[a]

def union_parent(parent, a, b):
	# 두 노드의 부모 노드를 두 부모 노드중에서 더 상단의 한 노드로 갱신하는 함수
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

n, e = map(int, input().split()) # 노드와 간선의 개수를 입력
parent = [0]*(n+1) # 부모 테이블

for i in range(1, n+1): # 각 노드의 부모를 자기 자신 노드로 초기화하는 과정
	parent[i] = i

for i in range(e):
	# 간선의 정보를 입력받는 과정
	# a 노드와 b 노드를 연결하는 과정
	# 두 노드가 이어졌을 때 두 노드 중에서 숫자가 적은 노드가 더 상단의 노드이다.
	a, b = map(int, input().split())
	union_parent(parent, a, b)

print("\nroot nodes")
for i in range(1, n+1):
	# i 노드의 부모 노드가 이어져있는 노드들 중에서 최상단 노드가 아닐 수 있기 때문에
	# 최상단 노드로 갱신해주는 작업
	find_parent(parent, i)
	print(parent[i], end=' ')

''' input data
6 4
1 4
2 3
2 4
5 6
Node, Edge
Start Node, End Node
'''