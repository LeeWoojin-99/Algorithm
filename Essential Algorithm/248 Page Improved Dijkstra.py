'''
248 Page
개선된 다익스트라 알고리즘
improved dijkstra algorithm
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
#n : 노드의 개수, m : 간선의 개수
#print(n, m) #test
start = int(input()) #시작 노드 번호 입력
graph = [[] for i in range(n+1)]
#노드의 번호를 인덱스로 하여 바로 리스트에 접근할 수 있도록 하기 위한 n+1
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False]*(n+1)
distance = [INF]*(n+1) #최단 거리 테이블을 모두 무한으로 초기화

for i in range(m):
    #모든 간선 정보를 반복
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = [] #힙 자료구조를 사용한 우선순위 큐 자료구조로 이용하기 위한 리스트 q를 생성
    heapq.heappush(q, (0, start))
    #heapq 라이브러리를 이용하여
    #시작 노드로 가기 위한 거리는 0으로 하여 q에 데이터 삽입
    distance[start] = 0
    #시작하는 곳에서 시작하는 곳까지의 거리는 0

    while q: #최단 거리가 가장 짧은 노드가 담기는 변수 q가 비지 않는다면 반복
        #시작 노드를 제외하고 노드의 개수만큼 반복
        dist, now = heapq.heappop(q)
        #우선순위가 가장 낮은(최단 거리가 가장 짧은) 노드를 변수 q에서 꺼내기
        #거리가 제일 짧은 노드를 반환
        #dist : 최단 거리
        #now : 노드의 위치

        if distance[now] < dist:
            print("now : %d\ndistance[now] : %d\ndist : %d"%(now, distance[now], dist))
            #현재 노드의 최단 거리로 기록된 데이터보다 최단거리가 클 때
            #이 조건문이 쓰이는 상황은 다음과 같다.
            # 이전에 방문했었던 노드에서 x번 노드를 탐색하면서 최단 거리 테이블의 거리 데이터를 갱신하여
            # x번 노드의 데이터를 q에 삽입
            # q에 담긴 노드들 중에서 최단 거리의 노드를 방문하는 동작을 진행하게 되는데
            # 진행되는 과정에서 x번 노드를 방문하게 되는데 방문하면 x번 노드까지의 최단 거리 데이터 탐색을 완료했다는 의미
            # 완료된 최단 거리 데이터가 있는 x번 노드를 다시 방문하게 되는 경우에 이 조건문이 쓰이게 된다.
            continue #방문된 노드일 경우 다시 q에서 데이터를 꺼내는 동작으로 회귀

        for i in graph[now]:
            #최단 거리를 갱신한 노드가 q에 들어가게 되는데
            #q의 노드들 중에서 가장 거리가 짧은 노드가 꺼내지는데 그 노드가 now번 노드
            #now번 노드에서 탐색을 진행하는 과정을 위한 for문
            cost = dist + i[1]
            #i[1] : now번 노드부터 i[0]번 노드까지의 거리 데이터
            #dist : 시작 노드로부터 now번 노드를 가기 전까지의 거리
            #cost : 시작 노드에서부터 i[0]번 노드까지의 거리

            if cost < distance[i[0]]:
                #now번 노드에서 i[0]노드로 탐색한 최단 거리가
                # 최단 거리 테이블의 거리 데이터보다 최적의 거리 일 경우
                distance[i[0]] = cost #최단 거리 테이블 갱신
                heapq.heappush(q, (cost, i[0]))
                #최단 거리 테이블을 갱신한 i[0]번 노드를 q에 삽입
        

dijkstra(start)

print()
for i in range(1, len(distance)):
    print("%d : %d"%(i, distance[i]))

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
'''
