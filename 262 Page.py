'''
262 Page
전보
Shortest Path Algorithm Problem
'''
''' 입력 및 출력 조건
입력 조건
첫째 줄 : 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C
둘째 ~ M+1번째 줄 : 통료에 대한 정보 X, Y, Z.
 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z.

출력 조건
첫째 줄 : 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 거리리는 시간을 공백으로 구분하여 출력
'''
''' 문제 풀이
시작하는 도시에서 모든 도시까지의 거리를 측정하여 가장 긴 거리를 구한다.
'''
''' 입력 예시
3 2 1
1 2 4
1 3 2
'''
import heapq

n, m, c = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    arr[x].append((y, z))

print()
for i in range(len(arr)):
    print("{} : {}".format(i, arr[i]))
print()

INF = 99
distance = [INF]*(n+1)
max = 0
count = 0
def dijkstra(start):
    global count, max
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            #i[0] : 목표 위치
            #i[1] : 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                if distance[i[0]] == INF: #도시를 처음 방문할 때마다 카운트
                    count += 1
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                if cost > max: #거리의 최고 값을 갱신
                    max = cost
dijkstra(c)
print(count, max)
