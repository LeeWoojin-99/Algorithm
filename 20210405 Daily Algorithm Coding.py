'''
2021. 04. 05.
Daily Algorithm Coding
Depth First Search Algorithm
Breath First Search Algorithm
'''
from collections import deque

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
visited = [False]*(len(graph)+1)
start =1

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visited[i]==False:
            dfs(graph, i, visited)


dfs(graph, start, visited)
print()


visited = [False]*(len(graph)+1)
q = deque([start])
visited[start] = True
while q:
    now = q.popleft()
    print(now, end=' ')
    for i in graph[now]:
        if visited[i] == False:
            q.append(i)
            visited[i] = True

print()

#중요한 특징
#DFS : 재귀 함수, 제일 먼 곳까지
#BFS : 큐, 가까운 곳부터