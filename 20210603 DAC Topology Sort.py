'''
2021. 06. 03.
Daily Algorithm Coding
Topology Sort Algorithm
'''
from collections import deque

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
start = 1

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

q = deque()

for i in range(1, n+1):
	if indegree[i] == 0:
		q.append(i)

while q:
	now = q.popleft()
	print(now, end=' ')

	for i in graph[now]:
		indegree[i] -= 1
		if indegree[i] == 0:
			q.append(i)




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