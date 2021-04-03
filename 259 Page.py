'''
259 Page
미래 도시
Shortest Path Algorithm Problem
'''

''' 문제 설명
방문 판매원 A
1번부터 N번까지의 회사
A는 1번에 위치. X번 회사에 방문해 물건을 판매하고자 한다.
연결된 2개의 회사는 양방향을 이동할 수 있다.
K번 회사에 존재하는 소개팅 상대와 만나고자 한다.

X번 회사에 가기 전에 K번 회사를 방문하고 X번 회사로 가고자 한다.
1 -> K -> X
'''

''' 입력 및 출력 조건
입력 조건
첫째 줄 : 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 입력
둘째 줄부터 M+1번째 줄 : 연결된 두 회사의 번호가 공백으로 구분되어 입력
M+2번째 줄 : X와 K가 공백으로 구분되어 차례대로 입력

출력 조건
첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력
만약 X번 회사에 도달할 수 없다면 '-1'을 출력
'''

import heapq
INF = 999
n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
#visited = [False]*(n+1)
distance = [INF]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
x, k = map(int, input().split())
print("\nn m x k")
print(n, m, x, k)
print("Graph Check")
for i in range(1, len(graph)):
    print("{} : {}".format(i, graph[i]))
print()
def DistanceCheck():
    for i in range(1, len(distance)):
        print("{} : {}".format(i, distance[i]))
    print()
print("Initial Distance")
DistanceCheck()

def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                heapq.heappush(q, (cost, i))
                distance[i] = cost

Dijkstra(1)
print("1 to k : %d"%distance[k])
DistanceCheck()
result = distance[k]


distance = [INF]*(n+1)
Dijkstra(k)
result += distance[x]
print("k to x : %d"%distance[x])
DistanceCheck()

if result < 999:
    print("1 - k - x : %d"%result)
else:
    print("-1")

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''
'''
4 2
1 3
2 4
3 4
'''