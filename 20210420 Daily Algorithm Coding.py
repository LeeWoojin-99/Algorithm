'''
2021. 04. 20.
Daily Algorithm Coding
Dijkstra Algorithm
'''
import heapq

INF = 999
n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for i in range(e):
	x, y, dist = map(int,input().split())
	graph[x].append((y, dist))

def dijkstra(start):
	queue = []
	heapq.heappush(queue, (0, start))
	distance[start] = 0

	while queue:
		dist, now = heapq.heappop(queue)

		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(queue, (cost, i[0]))

dijkstra(start)
print(distance)


''' dijkstra input data
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