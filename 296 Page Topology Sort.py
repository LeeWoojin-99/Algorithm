'''
296 Page
위상 정렬
Topology sort
'''
'''
진입 차수 : 노드에 진입하는 간선의 개수
진입 차수가 0인 것을 큐에 넣는 동작을 반복하며 위상을 정렬할 수 있다.
큐에 들어간 순서가 위상 정렬된 결과값이다.
'''

from collections import deque

v, e = map(int, input().split())
indegree = [0]*(v+1)
#in degree : 진입 차수
graph = [[] for i in range(v+1)]

for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1 

def topology_sort():
	#위상 정렬 함수
	result = []
	q = deque()

	for i in range(1, v+1):
		if indegree[i] == 0:
			q.append(i)

	while q:
		now = q.popleft()
		result.append(now)

		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				q.append(i)

	for i in result:
		print(i, end=' ')

topology_sort()

'''
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