'''
Daily Algorithm Coding
2021. 03. 30.
Dijkstra Algorithm
'''
import heapq

INF = 999
n, m = map(int, input().split())
distance = [INF]*(n+1)
visited = [False]*(n+1)
start = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print("\ninput data test")
print("n, m, start : %d, %d, %d"%(n, m, start))
print("graph")
for i in range(len(graph)):
    print("{} : {}".format(i, graph[i]))
print("{} : {}".format('distance', distance))
print("{} : {}\n".format('visited', visited))

def get_smallest_node():
    min_value = INF
    #최소값을 갱신하기 위한 변수 min_value
    index = 0
    for i in range(1, n+1):
        #방문하지 않은 노드 중에서
        #거리가 제일 짧은 노드를 구하기 위한 반복문
        if distance[i] < min_value and not visited[i]:
            #최단 거리 테이블인 distance에서 최소값을 갱신하기 위한 변수 min_value보다 작은 경우
            #방문을 하지 않은 경우
            min_value = distance[i]
            #최소값을 갱신
            index = i
            #갱신할 때의 index값을 저장
    return index #방문하지 않은 노드 중에서 거리가 제일 짧은 노드를 반환

def Dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for x in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost

Dijkstra(start)
print("After Dijkstra Algorithm")
for i in range(1, len(distance)):
    print("{} : {}".format(i, distance[i]))

distance = [INF]*(n+1)
def ImprovedDijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    visited[start] = True

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

ImprovedDijkstra(start)
print("\nAfter Improved Dijkstra Algorithm")
for i in range(1, len(distance)):
    print("{} : {}".format(i, distance[i]))

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
