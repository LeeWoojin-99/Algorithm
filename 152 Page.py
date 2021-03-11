#152 Page 미로 탈출
''' 문제 설명
N x M 크기의 직사각형 형태의 미로
N : 가로
M : 세로

좌표 표현 : (y(세로), x(가로))
유저의 위치는 (1, 1)
미로의 출구는 (N, M)

0 : 괴물이 있는 부분
1 : 괴물이 없는 부분

유저는 (1, 1)부터 시작하여 괴물이 없는 부분만을 통과하여
미로의 출구인 (N, M)까지 도착해야 한다.

시작 지점으로부터 도착 지점까지 필요한 최소 이동 횟수를 구하시오.
'''
'''
더 많은 횟수로 도착하는 경우가 먼저 찾아질 수는 없는가 ?
없다. BFS로 구현한다면 가까운 경로를 차례대로 지우면서 탐색해가기 때문이다.
더 많은 횟수로 도착했던 곳에 중복되어 다시 도착하는 경우는 있다.
'''
''' 입력 예시
5 6
101010
111111
000001
111111
111111
'''

from collections import deque

N, M = list(map(int, input().split()))
arrMaze = []
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
for i in range(N):
    arrMaze.append(list(map(int, input())))

print(arrMaze)

def BFS(x, y):
    SearchQueue = deque()
    SearchQueue.append((x, y))
    while SearchQueue:
        x, y = SearchQueue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            print()
            print("x, y")
            print(x, y)
            print("nx, ny")
            print(nx, ny)
            if not(-1<nx<M and -1<ny<N):
                print("맵 이탈")
                continue
            elif arrMaze[ny][nx]==0:
                print("괴물")
                continue
            elif arrMaze[ny][nx]==1:
                arrMaze[ny][nx] = arrMaze[y][x] + 1
                print("첫 도달")
                print(arrMaze[ny][nx])
                SearchQueue.append((nx, ny))

BFS(0, 0)
print(arrMaze[N-1][M-1])

