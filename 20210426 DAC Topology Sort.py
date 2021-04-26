'''
2021. 04. 26.
Daily Algorithm Coding
topology sort
'''
from collections import deque

node, edge = map(int, input().split())
indegree = [0]*(node+1)
graph = [[] for _ in range(node+1)]

for i in range(edge):
	x, y = map(int, input().split())
	graph[x].append(y)
	indegree[y] += 1

queue = deque()

for i in range(1, node+1):
	if indegree[i] == 0: queue.append(i)

while queue:
	now = queue.popleft()
	print(now, end=' ')

	for i in graph[now]:
		indegree[i] -= 1
		if indegree[i] == 0: queue.append(i)


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