'''
355 Page
처음부터 끝까지 내 힘으로 풀이하여 코딩
'''

from collections import deque

def check_map(check_map_data):
    print("check map function")
    for y in range(len(check_map_data)):
        for x in range(len(check_map_data)):
            print(check_map_data[y][x], end=' ')
        print()
    print()

def move_check(map, robot_1, robot_2, count):
    # 입력된 로봇의 위치에서 이동할 수 있는 곳만을 걸러내는 함수
    result = []

    # 이동할 때 쓰이는 값
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(4):# 네 방향으로 이동
        new_position_1 = (robot_1[0]+dy[i], robot_1[1]+dx[i]) # new_position : 로봇이 이동한 좌표
        new_position_2 = (robot_2[0]+dy[i], robot_2[1]+dx[i])

        # 로봇이 이동한 좌표가 안전한지 검사
        if map[new_position_1[0]][new_position_1[1]] == 0 and map[new_position_2[0]][new_position_2[1]] == 0:
            result.append((count+1, new_position_1, new_position_2)) # 안전하다면 결과에 추가

    return result

def rotate_check(map, robot_1, robot_2, count):
    # 입력된 로봇의 위치에서 회전했을 때 안전한 위치만을 걸러내는 함수
    result = []

    if robot_1[0] == robot_2[0]: # 가로
        for rotate in [-1, 1]: # 위 아래
            if map[robot_1[0]+rotate][robot_1[1]] == 0 and map[robot_2[0]+rotate][robot_2[1]] == 0:
                result.append((count+1, robot_1, (robot_1[0]+rotate, robot_1[1]))) # robot_1을 중심으로 회전
                result.append((count+1, robot_2, (robot_2[0]+rotate, robot_2[1]))) # robot_2를 중심으로 회전
            
    else: # 세로
        for rotate in [-1, 1]: # 왼쪽 오른쪽
            if map[robot_1[0]][robot_1[1]+rotate] == 0 and map[robot_2[0]][robot_2[1]+rotate] == 0:
                result.append((count+1, robot_1, (robot_1[0], robot_1[1]+rotate))) # robot_1을 중심으로 회전
                result.append((count+1, robot_2, (robot_2[0], robot_2[1]+rotate))) # robot_2를 중심으로 회전

    #print("result rotate")
    #print(result)
    return result


def solution(board):

    n = len(board)
    count = 0

    map = [[1]*(n+2) for _ in range(n+2)]
    for y in range(n):
        for x in range(n):
            map[y+1][x+1] = board[y][x]
    #check_map(map)

    robot_1 = (1,1)
    robot_2 = (1,2)
    # y, x

    q = deque()
    q.append((0, robot_1, robot_2))
    visited = set((robot_1, robot_2))

    while 1:
        count, robot_1, robot_2 = q.popleft()
        #print("\ncount : {}\nrobot_1 : {}\nrobot_2 : {}".format(count, robot_1, robot_2))
        #print("visited :", visited)
        #print("map")
        #print(map[robot_2[0]][robot_2[1]])

        if robot_1 == (n, n) or robot_2 == (n, n): return count # 목표 지점에 로봇이 도달했다면 종료

        possibility = [] # robot의 현재 위치에서 이동할 수 있는 위치들이 담길 공간
        for i in move_check(map, robot_1, robot_2, count): possibility.append(i)
        for i in rotate_check(map, robot_1, robot_2, count): possibility.append(i)

        for i in possibility:
            if (i[1], i[2]) not in visited:
                q.append(i)
                visited.add((i[1], i[2]))
        #print("q :", q)

#print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))

'''
1 1 1 1 1 1 1 
1 0 0 0 1 1 1 
1 0 0 0 1 0 1 
1 0 1 0 1 1 1 
1 1 1 0 0 1 1 
1 0 0 0 0 0 1 
1 1 1 1 1 1 1 

0 0 0 1 1 1 1
0 0 0 0 0 0 0
0 1 0 1 1 1 0
1 1 0 1 1 1 0
0 1 0 0 1 1 0
0 0 0 0 0 0 0
1 1 1 1 1 0 0

[0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 1],
[1, 1, 0, 1, 1, 1],
[0, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0]

0 0 0 1 1 1 1
0 0 0 0 0 0 0
0 1 0 1 1 1 0
1 1 0 1 1 1 0
0 1 0 0 1 1 0
0 0 0 0 0 0 0
1 1 1 1 1 0 0

    [
    [0, 0, 0, 0, 0, 0, 1], 
    [1, 1, 1, 1, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 1, 1, 0], 
    [0, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 1, 1], 
    [0, 0, 1, 0, 0, 0, 0]
    ]
'''