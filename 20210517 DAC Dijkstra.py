'''
2021. 05. 17.
Daily Algorithm Coding
Dijkstra Algorithm
'''
import heapq

def distance_check():
	print("distance check function")
	for i in range(1, len(distance)):
		print(distance[i], end=' ')
	print()

n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [999]*(n+1)

for _ in range(e):
	a, b, dist = map(int, input().split())
	graph[a].append((b, dist))

distance_check()

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
	dist, now = heapq.heappop(q)

	if distance[now] < dist: continue

	for i in graph[now]:
		cost = dist + i[1]

		if cost < distance[i[0]]:
			distance[i[0]] = cost
			heapq.heappush(q, (cost, i[0]))

distance_check()


'''
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
'''