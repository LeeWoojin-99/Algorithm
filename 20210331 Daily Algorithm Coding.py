'''
2021. 03. 31.
Daily Algorithm Coding
'''
import heapq
INF = 999
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def Dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

def ImprovedDijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

print()

Dijkstra(start)
print("Dijkstra")
for i in range(1, len(distance)):
    print("%d : %d"%(i, distance[i]))
print()

distance = [INF]*(n+1)
ImprovedDijkstra(start)
print("ImprovedDijkstra")
for i in range(1, len(distance)):
    print("%d : %d"%(i, distance[i]))
print()


''' 입력 예시
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