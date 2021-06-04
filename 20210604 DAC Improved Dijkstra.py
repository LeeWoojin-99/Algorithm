'''
2021. 06. 04.
Daily Algorithm Coding
Improved Dijkstra Algorithm
'''

import heapq

n, e, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [999]*(n+1)

for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

distance[start] = 0
q = []
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist: continue

    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            heapq.heappush(q, (cost, i[0]))
            distance[i[0]] = cost

print("\ndistance")
for i in range(1, n+1): print(distance[i], end=' ')
print()

'''
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
node edge start
edge data
edge data : start node, end node, distance
'''