#Breath First Search
#너비 우선 탐색
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    #deque 메소드의 인수값으로는 iterable을 받기 때문에
    #start라는 인수값 변수를 요소로서 []에 담아서 사용
    visited[start] = True
    #방문 처리
    while queue:
        #queue가 빌 때까지
        v = queue.popleft()
        #가장 먼저 들어온 요소값을 빼서 변수 v에 대입
        print(v, end=' ')
        for i in graph[v]:
            #queue에서 빼서 v에 담은 노드의 인접 노드
            if not visited[i]:
                #그 노드들 중에서 방문한 적이 없는 노드
                queue.append(i)
                #queue에 추가
                visited[i] = True
                #방문 처리

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
#BFS : 1 2 3 8 7 4 5 6
visited = [False]*9
bfs(graph, 1, visited)
print()