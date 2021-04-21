'''
2021. 04. 21.
Daily Algorithm Coding
Dijkstra
Floyd Washall
'''
import heapq


#Dijkstra Algorithm Code

n, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [99]*(n+1)
queue = []

for i in range(e):
	x, y, dist = map(int, input().split())
	graph[x].append((y, dist))

heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
	dist, now = heapq.heappop(queue)
	#print(dist, now) # test

	for i in graph[now]:
		cost = dist + i[1]

		if cost < distance[i[0]]:
			distance[i[0]] = cost
			heapq.heappush(queue, (cost, i[0]))

print("Dijkstra")
for i in range(1, len(distance)): print(distance[i], end=' ')
print()


#Floyd Washall Algorithm Code

n, e = map(int, input().split())
distance = [[99]*(n+1) for _ in range(n+1)]

for i in range(e):
	x, y, dist = map(int, input().split())
	distance[x][y] = dist


for i in range(n+1):
	distance[i][i] = 0

for k in range(n+1):
	for i in range(n+1):
		for j in range(n+1):
			distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

print("Floyd Washall")
for i in range(1, len(distance)):
	print("%d :"%i, end='')
	for j in range(1, len(distance)):
		print("{:3}".format(distance[i][j]), end='')
	print()
print()

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
node edge
start node
edge data
edge data : start node, end node, distance
'''
'''
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
node edge
edge data
edge data : start node, end node, distance
'''
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
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''