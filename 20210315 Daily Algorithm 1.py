#2021 03 15
#DFS, BFS, Selection Sort 연습
from collections import deque

graph = [
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

def DFS(graph, start, visited):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if visited[i]==False:
            DFS(graph, i, visited)

def BFS(garph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i] = True
                
visited = [False]*9
print("Depth First Search")
DFS(graph, 1, visited)
print()
visited = [False]*9
print("\nBreath First Search")
BFS(graph, 1, visited)
print("\n")

Arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print("Selection Sort")
print(Arr)
for i in range(len(Arr)):
    min = i
    for j in range(1, len(Arr)):
        if Arr[min]>Arr[j]:
            min = j
    Arr[min], Arr[j] = Arr[j], Arr[min]
print(Arr)
print("")