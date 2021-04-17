'''
2021. 04. 16.
Daily Algorithm Coding
DFS/BFS
Depth First Search
Breath First Search
'''
from collections import deque
#Queue 자료구조를 사용하기 위한 라이브러리 deque

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
length = len(graph) #graph 리스트의 요소의 개수
visited = [False]*length
start = 1


#DFS Code
def DFS(v, graph, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == False:
            DFS(i, graph, visited)

DFS(start, graph, visited)
print()


#BFS Code
visited = [False]*length

queue = deque([start])
while queue:
    v = queue.popleft()
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == False:
            queue.append(i)
            visited[i] = True
