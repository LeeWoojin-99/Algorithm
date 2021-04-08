'''
2021. 04. 08.
Daily Algorithm Coding

Shortest Path Algorithm
1. Dijkstra Algorithm
2. Floyd Washall Algorithm

Search Algorithm
1. Depth First Search
2. Breath First Search
'''
import heapq
from collections import deque

#Dijkstra Algorithm Code
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [999]*(n+1)
for i in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def DistanceCheck():
	for i in range(1, len(distance)):
		print("{} : {}".format(i, distance[i]))

def Dijkstra(start):
	q = []
	distance[start] = 0
	heapq.heappush(q, (0, start))
	while q:
		dist, now = heapq.heappop(q)
		if distance[now] < dist: continue
		for i in graph[now]:
			cost = dist + i[1]
			if distance[i[0]] > cost:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

print()
print("Dijkstra Algorithm")
print("Basis Distance Data")
DistanceCheck()
Dijkstra(start)
print("Distance Data Using Dijkstra Algorithm")
DistanceCheck()

#Floyd Washall Algorithm Code
n, m = map(int, input().split())
start = int(input())
graph = [[999]*(n+1) for i in range(n+1)]

def GraphCheck():
	for i in range(1, len(graph)):
		print("{} : {}".format(i, graph[i]))

print("\nFloyd Washall Algorithm")
print("Basis Graph Data")
GraphCheck()

for i in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = c

print("Graph Data Using Edge Data")
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
edge data : start node, end node, distance
'''
''' Floyd Washall Algorithm 입력 예시
4 7
1
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

node edge
start node
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
1
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

graph = [
#DFS/BFS graph data
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False]*(len(graph)+1)
start = 1

#Depth First Search Algorithm Code
def DFS(graph, v, visited):
	visited[v] = True
	print(v, end=' ')
	for i in graph[v]:
		if visited[i]==False:
			DFS(graph, i, visited)
print("\nDepth First Search Algorithm")
DFS(graph, start, visited)
print()

#Breath First Search Algorithm Code
visited = [False]*(len(graph)+1)
q = deque([start])
visited[start] = True

print("Breath Frist Search Algorithm")
while q:
	v = q.popleft()
	print(v, end=' ')
	for i in graph[v]:
		if visited[i]==False:
			q.append(i)
			visited[i] = True

#DFS : 1 2 7 6 8 3 4 5
#BFS : 1 2 3 8 7 4 5 6