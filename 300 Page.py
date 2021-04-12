'''
300 Page
도시 분할 계획
Graph Algorithm Problem

문제 설명
마을의 집 개수 N, 그 집들을 연결하는 M개의 길
마을 이장은 마을을 2개의 분리된 마을로 분할할 계획
각 분리된 마을 안에는 임의의 두 집 사이에 길이 항상 존재해야 한다.
각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서
길을 최대한 없애려 한다.
마을의 이장은 길을 최대한 없애서 길의 유지비의 합을 최소로 하고 싶다.
최소 유지비의 합을 구하시오.

문제 풀이
최소 신장 트리를 이용한다.
분리된 마을간의 최소 신장 트리를 구하면 되는데
마을을 분리는 어떻게 할 것인가?
마을을 분리하지 않고 구한 최소 신장 트리에서 제일 비용이 높은 길을 없앤다.
그 길을 기준으로 마을이 분리된다.

입력 조건
첫째 줄 : 집의 개수 N, 길의 개수 M
그 다음 M개의 줄 : A, B, C : A번 집과 B번 집을 연결하는 길의 유지비가 C.

출력 조건
길을 없애고 남은 유지비의 합의 최솟값을 출력
'''


def dss_find(parent, x):
	if parent[x] != x:
		parent[x] = dss_find(parent, parent[x])
	return parent[x]

def dss_union(parent, x, y):
	x = dss_find(parent, x)
	y = dss_find(parent, y)
	if x < y:
		parent[y] = x
	else:
		parent[x] = y

node, edge = map(int, input().split())
parent = [0]*(node+1)

edge_data = []
total_distance = 0
max_distance = 0

for i in range(node+1):
	parent[i] = i

for _ in range(edge):
	x, y, dist = map(int, input().split())
	edge_data.append((dist, x, y))

edge_data.sort()

for i in edge_data:
	dist, x, y = i

	if dss_find(parent, x) != dss_find(parent, y):
		dss_union(parent, x, y)

		total_distance += dist

		max_distance = dist

print("result : ", end = '')
print(total_distance - max_distance)


''' input data
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''