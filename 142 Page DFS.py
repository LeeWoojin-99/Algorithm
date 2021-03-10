#Depth-First Search
#깊이 우선 탐색
def dfs(graph, v, visited):
    visited[v] = True
    #현재 노드 v
    #현재 노드를 방문 처리하였다.
    print(v, end=' ')
    #방문했던 노드의 순서를 알기 위한 출력문
    for i in graph[v]:
        #현재 노드의 인접 노드를 방문
        if not visited[i]:
            #인접 노드중에서 방문하지 않았던 노드
            dfs(graph, i, visited)
            #그 노드에서 탐색을 이어가기 위해서
            #해당 노드에서 탐색하는 함수를 재귀적으로 호출

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
visited = [False]*9
dfs(graph, 1, visited)
print()