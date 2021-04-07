'''
2021. 04. 07.
Daily Algorithm Coding
Search Algorithm
Depth First Search Algorithm
Breath First Search Algorithm
'''
from collections import deque

#Depth First Search Algorithm Code
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
visited = [False]*(len(graph)+1)
start = 1

def DFS(graph, vn, visited):
	#vn : visiting node
	visited[vn] = True
	print(vn, end=' ')
	for i in graph[vn]:
		if visited[i] == False:
			DFS(graph, i, visited)

print("Depth First Search Algorithm")
DFS(graph, start, visited)
print()

print("Breath First Search Algorithm")
visited = [False]*(len(graph)+1)
queue = deque([start])
visited[start] = True
while queue:
	vn = queue.popleft()
	print(vn, end=' ')
	for i in graph[vn]:
		if visited[i] == False:
			queue.append(i)
			visited[i] = True


#DFS : 1 2 7 6 8 3 4 5
#BFS : 1 2 3 8 7 4 5 6