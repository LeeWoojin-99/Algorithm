'''
2021. 04. 02.
Daily Algorithm Coding
Dijkstra Algorithm
Floyd Washall Algorithm
'''
import heapq

INF = int(99)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

def GraphCheck():
    print("\nGraph Check")
    for i in range(1, len(graph)):
        for j in range(1, len(graph[i])):
            print("{:3}".format(graph[i][j]), end=' ') 
        print()
    print()

GraphCheck()

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

GraphCheck()

''' Floyd Washall Algorithm 입력 예시
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def DistanceCheck():
    print("\nDistance Check")
    for i in range(1, len(distance)):
        print("{} : {}".format(i, distance[i]))
    print()

def ImprovedDijkstra(start):
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

DistanceCheck()
ImprovedDijkstra(start)
DistanceCheck()

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
'''

''' 통합 입력 예시
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
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