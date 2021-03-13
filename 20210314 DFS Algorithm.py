#2021 03 14
#DFS (Depth First Search)
#깊이 우선 탐색
#연습

graph = [
    #인덱스를 노드, 그 인덱스의 요소가 해당 노드의 인접 노드
    #인접 리스트 방식으로 그래프를 표현
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i]==False:
            DFS(graph, i, visited)

visited = [False]*9
DFS(graph, 1, visited)
print()

''' 중요 포인트
재귀 함수

호출된 곳에 연결된 곳이 방문한 곳이 맞다면
재귀적으로 호출하여 탐색
'''