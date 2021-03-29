'''
237 Page
easy dijkstra algorithm
'''
import sys
input = sys.stdin.readline
#변수에 함수명을 넣을 수 있다.
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

def dijkstra(start):
    distance[start] = 0
    #시작하는 곳에서 시작하는 곳까지의 거리는 0
    visited[start] = True
    #시작하는 곳을 방문 처리

    for j in graph[start]:
        #시작하는 지점을 방문하고 인접한 노드를 탐색
        #시작 지점에서 j[0]번 노드로 가는 비용이 j[1]
        distance[j[0]] = j[1]

    for i in range(n-1):
        #시작 노드를 제외하고 노드의 개수만큼 반복
        now = get_smallest_node()
        #변수 now에 방문하지 않은 노드 중에서 거리가 제일 짧은 노드를 반환
        visited[now] = True
        #반환받은 노드를 방문 처리

        for j in graph[now]:
            #반환받은 노드에서 j[0]번 노드로 가는 비용이 j[1]
            cost = distance[now] + j[1]
            #시작 지점에서부터 j[0]번 노드까지의 거리
            if cost < distance[j[0]]:
                #만약 최단 거리 테이블인 distance에서의 거리보다 cost가 더 작을 경우
                distance[j[0]] = cost
                #최단 거리 테이블를 갱신

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
