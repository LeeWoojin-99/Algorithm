'''
339 Page
특정 거리의 도시 찾기
DFS/BFS Algoroithm Problem
'''
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
distance = [0]*(n+1)

for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)

queue = deque([x])
visited[x] = True
distance[x] = 0

print("\n결과값")
while queue:
	v = queue.popleft()

	for i in graph[v]:
		if visited[i] == False:
			queue.append(i)
			visited[i] = True

			distance[i] = distance[v]+1
			if distance[i] == k:
				print(i)


''' input data
4 4 2 1
1 2
1 3
2 3
2 4

4 4 1 1
1 2
1 3
2 3
2 4
'''