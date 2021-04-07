'''
2021. 04. 07.
Daily Algorithm Coding
Shortest Path Algorithm
1. Dijkstra Algorithm
2. Floyd Washall Algorithm
'''

#Dijkstra Algorithm Code
import heapq
INF = 999
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
start = int(input())
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def Dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

def DistanceCheck():
	for i in range(1, len(distance)):
		print("{} : {}".format(i, distance[i]))

def GraphCheck():
	for i in range(1, len(graph)):
		print("{} : {}".format(i, graph[i]))

print("\nDikstra Algorithm\nBasic Distance Data")
DistanceCheck()
Dijkstra(start)
print("Distance Data Using Dijkstra Algorithm")
DistanceCheck()
print()

#Floyd Washall Algorithm Code
n, m = map(int, input().split())
graph = [[INF]*(n+1) for i in range(n+1)]
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c
print("Floyd Washall Algorithm\nGraph Data Using Edge Data")
GraphCheck()
for k in range(n+1):
	for i in range(n+1):
		for j in range(n+1):
			graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
print("Graph Data Using Floyd Washall Algorithm")
GraphCheck()



''' Dijkstra 입력 예시
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
'''
''' Floyd Washall Algorithm 입력 예시
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

node
edge
edge data
edge data : start node, end node, distance
'''
''' 통합 입력 예시
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
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''