'''
2021. 05. 08.
Daily Algorithm Coding
Dijkstra Algorithm
최단거리 찾기
'''
import heapq

n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [999]*(n+1)

for _ in range(e):
	a, b, dist = map(int, input().split())
	graph[a].append((b,dist))

q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
	dist, now = heapq.heappop(q)

	if dist > distance[now]: continue

	for i in graph[now]:
		cost = dist + i[1]
		if cost < distance[i[0]]:
			distance[i[0]] = cost
			heapq.heappush(q, (cost, i[0]))

print(distance)

''' input data
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
node edge
start node
edge data
edge data : start node, end node, distance
'''
''' answer
0 2 3 1 2 4
'''