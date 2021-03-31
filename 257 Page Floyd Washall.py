'''
257 Page
Floyd Washall Algorithm
'''

INF = int(99)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

def GraphCheck():
    print("\nGraph Check")
    for i in range(1, len(graph)):
        for j in range(1, len(graph[i])):
            print("{:3}".format(graph[i][j]), end=' ')
        print()
    print()

for i in range(1, n+1):
    #graph에서 자기 자신에서 자기 자신까지 가는 거리를 0으로 설정
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0


GraphCheck()

for _ in range(m): #노드와 간선 입력
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드까지의 거리 c
    graph[a][b] = c
    #간선 데이터를 graph에 갱신

GraphCheck()

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            #k번 노드를 거쳐가는 모든 경로를 비교한다.
            #a번 노드에서 b번 노드까지의 거리
            #a번 노드에서 k번 노드를 거치는 b번 노드까지의 거리
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

GraphCheck()

'''
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