'''
2021. 05. 18.
Daily Algorithm Coding
Depth First Search
'''

#basis data
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
#DFS : 1 2 7 6 8 3 4 5
#BFS : 1 2 3 8 7 4 5 6


# Depth First Search Algorithm Code
visited = [False]*len(graph)
start = 1

print("DFS : ", end='')
def dfs(v, graph, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, graph, visited)

dfs(start, graph, visited)
print()