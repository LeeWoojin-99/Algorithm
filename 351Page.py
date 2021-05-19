'''
351 Page
감시 피하기
DFS/BFS Algorithm Problem
'''
'''
모든 벽 설치 경우에 대한 감시 회피 여부를 체크
'''

import itertools

def watch_check(map_data, teacher_positions):

    for teacher_position in teacher_positions: # 각 선생님이 학생을 발견하는지 확인하는 반복문
        for direction in directions:
            # direction : 현재 검사하고 있는 방향

            check_position = list(teacher_position)
            # 방향마다 teacher_position에서 시작해야 하므로 check_position으로 사용

            while 1:
                check_position[0] += direction[0] # x 좌표 이동
                check_position[1] += direction[1] # y 좌표 이동

                if not(0 <= check_position[0] < n and 0<= check_position[1] <n): break

                # 이동된 좌표에 학생이 있는지 검사
                if map_data[check_position[1]][check_position[0]] == 's':
                    return 'No'
                elif map_data[check_position[1]][check_position[0]] == 'o': break

    return 'Yes'
    


n = int(input())
map_data = [[] for _ in range(n)]
x_positions_list = []
teacher_positions_list = []
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# x, y
# 상 하 좌 우
# 위 아래 왼쪽 오른쪽

for y in range(n):
    input_data = input().split()
    for x in range(n):
        map_data[y].append(input_data[x])
        if input_data[x] == 'x': # 빈 공간의 좌표를 저장
            x_positions_list.append((x, y))
            # (x, y) 형태로 저장
        elif input_data[x] == 't': # 선생님의 좌표를 저장
            teacher_positions_list.append((x, y))

''' map data check '''
def map_data_check():
    for y in range(n):
        print(map_data[y])

x_cases = list(itertools.permutations(x_positions_list, 3))

for x_case in x_cases:
    # x_case : 장애물이 되어야하는 좌표 3개가 담긴 튜플
    #print(x_case) #TEST
    for position_x_to_o in x_case:
        # position_x_to_o : 빈 공간에서 장애물이 되어야하는 좌표 1개
        #print(position_x_to_o) #TEST
        map_data[position_x_to_o[1]][position_x_to_o[0]] = 'o' # 장애물로 변환

    # 함수 실행
    result = watch_check(map_data, teacher_positions_list)
    if result == 'Yes':
        break

    for position_x_to_o in x_case: # 빈 공간에서 장애물이 되었던 것을 원래대로 되돌린다.
        map_data[position_x_to_o[1]][position_x_to_o[0]] = 'x'

print(result)

'''
5
x s x x t
t x s x x
x x x x x
x t x x x
x x t x x

3
x s x
t x s
x x x

4
s s s t
x x x x
x x x x
t t t x
'''