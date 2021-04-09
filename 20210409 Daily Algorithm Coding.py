'''
2021. 04. 09.
Daily Algorithm Coding
Shortest Path Algorithm
 1. Dijkstra
 2. Floyd Washall
'''
import heapq

#Dijkstra Algorithm Code
num_node, num_edge = map(int, input().split())
start = int(input())
graph = [[] for i in range(num_node+1)]
distance = [999]*(num_node+1)

for i in range(num_edge):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

def distance_check():
	for i in range(1, len(distance)):
		print("{} : {}".format(i, distance[i]))

def dijkstra(start):
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
dijkstra(start)
distance_check()


#Floyd Washall Algorithm Code
num_node, num_edge = map(int, input().split())
start = int(input())
graph = [[999]*(num_node+1) for i in range(num_node+1)]

for i in range(num_edge):
	a, b, c = map(int, input().split())
	graph[a][b] = c

def graph_check():
	for i in range(1, len(graph)):
		print("{} : {}".format(i, graph[i]))

graph_check()
for k in range(num_node+1):
	for i in range(num_node+1):
		for j in range(num_node+1):
			graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
graph_check()





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
''' 정답
Dijkstra
1 : 0
2 : 2
3 : 3
4 : 1
5 : 2
6 : 4

Floyd Washall
1 : [999, 7, 4, 8, 6]
2 : [999, 3, 7, 7, 9]
3 : [999, 5, 9, 6, 4]
4 : [999, 7, 11, 2, 6]
'''