#2021.03.14. BFS 연습
#Breath First Search
#너비 우선 탐색

from collections import deque

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[v] = True
        print(v, end=' ')

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
BFS(graph, 1, visited)
print("")

''' 중요 포인트
from collections import deque
while queue
queue.popleft()
queue.append()
if visited[i]==False
visited[v] = True
'''