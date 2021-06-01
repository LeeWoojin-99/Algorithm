'''
2021. 06. 01.
Daily Algorithm Coding
Dijkstra Algorithm
최단 거리를 알아낼 수 있는 알고리즘
'''
import heapq

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node+1)]
distance = [999]*(node+1)

for i in range(edge):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

queue = []
heapq.heappush(queue, (0, start))
distance[start] = 0

while queue:
    dist, now = heapq.heappop(queue)

    if distance[now] < dist: continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0]))

print("result")
for i in range(1, node+1):
    print(distance[i], end=' ')
print()

''' INPUT DATA
6 11 1
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