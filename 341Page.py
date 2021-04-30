'''
341 Page
연구소
DFS/BFS Algorithm Problem
'''
''' 문제 설명
연구소에서 바이러스의 확산을 막기 위해서 벽을 세우려고 한다.
바이러스는 상하좌우 인접한 빈칸으로 퍼져나간다.
새로 세울 수 있는 벽의 개수는 3개이다.

n, m : 지도의 세로, 가로 크기
0 빈칸, 1 벽, 2 바이러스
빈칸의 개수는 3개 이상
바이러스의 개수는 2개 이상, 10 이하

얻을 수 있는 안전영역의 최대 크기를 구하시오
'''
'''
바이러스가 사방으로 퍼져나간다 => BFS 알고리즘을 이용하여 퍼져나가는 것을 구현할 수 있다.
DFS/BFS 알고리즘을 이용하여 벽이 쳐져있을 때의 안전영역의 크기를 알 수 있다.
빈칸에 벽 3개를 세우는 모든 경우의 수에 따른 안전 영역의 크기를 구한다? => 너무 많은 연산이 필요하다.
3 <= 가로 세로 <= 8
2 <= 바이러스 <= 10
3 <= 빈칸

빈칸에 벽 3개를 세우는 모든 경우의 수에 따른 안전 영역의 크기 구하기.

3중 for문
벽1 -> 벽2 -> 벽3
벽1이 최상위 for문

안전 영역의 크기 구하기
안전 영역의 크기를 담는 변수 safety_zone

0에서부터 길찾기를 시작.
길을 찾으면서 방문하는 0의 개수를 세는 변수 count

길을 찾아가는 도중에 바이러스를 만난다면 break
바이러스를 만나지 않고 길찾기를 완료하였다면 만난 safety_zone += count

안전 영역의 크기를 구하였다면 result에 넣기

'''
from collections import deque


def zero_order_check(map_data, count):
	# 지도에서 count번째 빈칸을 찾아 좌표를 반환하는 함수
	for y in range(len(map_data)):
		for x in range(len(map_data[y])):
			if map_data[y][x] == 0:
				count -= 1
				if count == 0: return x, y
	return None, None

def find_way(map_data):
	# 안전 영역의 크기 구하여 반환하는 함수
	queue = deque() # 시작 좌표를 큐 자료구조에 삽입
	visited = [[False]*len(map_data[0]) for _ in range(len(map_data))]
	count = 1 # 길을 찾으면서 방문한 빈칸의 개수. 시작 좌표가 있으니 1로 초기화.
	safety_zone = 0
	find_way_good = False
	virous = False

	for y in range(len(map_data)):
		for x in range(len(map_data[0])): # 한 칸씩 빈칸이 있는지 확인한다.
			#print("\n")
			#print("x, y 좌표 : %d, %d"%(x, y))
			#print("%d"%map_data[y][x])
			#print("")
			count = 1
			find_way_good = False
			virous = False

			if visited[y][x] == False and map_data[y][x] == 0: # 방문하지 않은 빈칸 발견
				#print("빈칸 발견")
				queue.append((x, y))
				visited[y][x] = True
				find_way_good = True

			while queue: # 발견한 빈칸으로부터 길찾기
				#print("길 찾기")
				v_x, v_y = queue.popleft()

				for direction in direction_list:
					# 해당 방향으로 한 칸 이동한 좌표'''
					#print(v_x, v_y)
					v_x += direction[0]
					v_y += direction[1]
					#print("이동 후 : %d, %d"%(v_x, v_y))
					if not(0 <= v_x <= len(map_data[0])-1 and 0 <= v_y <= len(map_data)-1):
						v_x -= direction[0]
						v_y -= direction[1]
						continue # 맵을 넘어가는 좌표라면 다른 방향으로 넘어가기
					if map_data[v_y][v_x] == 0 and visited[v_y][v_x] == False: # 방문하지 않은 빈칸이라면 방문하기
						#print("방문하지 않은 곳 방문")
						'''
						for vvy in range(len(visited)):
							for vvx in range(len(visited[vvy])):
								if visited[vvy][vvx] == True:
									print("1", end=' ')
								else:
									print("0", end=' ')
							print()
						'''

						queue.append((v_x, v_y))
						visited[v_y][v_x] = True
						count += 1
					if map_data[v_y][v_x] == 2: # 길을 찾다가 바이러스와 만난다면
						#print("바이러스를 만남")
						virous = True
					# 해당 방향으로 한 칸 이동했던 좌표를 되돌림
					v_x -= direction[0]
					v_y -= direction[1]

			if find_way_good == True and virous == False:
				#print("count : %d"%count)
				safety_zone += count
				# print("safety_zone : %d"%safety_zone)
				# 방문하지 않은 빈칸을 발견하지 못하였는데도 카운트가 더해지는 문제
			#print()
		#print()

	return safety_zone

y, x = map(int, input().split())
map_data = []
visited = [[False]*x in range(y)]
direction_list = [(0, -1), (1, 0), (0, 1), (-1, 0)] # (x, y). 위쪽 오른쪽 아래쪽 왼쪽
result = []
# 맵 데이터 입력
for i in range(y):
	data = list(map(int, input().split()))
	map_data.append(data)

# map_data check
def map_check(map_data):
	print("map data check")
	for y in range(len(map_data)):
		for x in range(len(map_data[y])):
			print(map_data[y][x], end=' ')
		print()

# 0의 개수 세기
max_zero_order = 0
for y in range(len(map_data)):
	for x in range(len(map_data[y])):
		if map_data[y][x] == 0:
			max_zero_order += 1
max_zero_order -= 2
'''
print("func test")
map_check(map_data)
print(zero_order_check(map_data, 35))
x, y = zero_order_check(map_data, 35)
print(map_data[y][x])
map_data[y][x] = 1
print(map_data[y][x])
map_check(map_data)
print("func test")
'''
'''
#print("func\nfunc\nfunc\nfunc")
map_check(map_data)
map_data[0][1] = 1
map_data[1][0] = 1
map_data[3][5] = 1
map_check(map_data)
#print(find_way(map_data))
#print("func\nfunc\nfunc\nfunc")
'''

wall_order_list = [0]*3
for wall_first in range(1, max_zero_order):
	#print("wall_1 : %d"%wall_first)
	x, y = zero_order_check(map_data, wall_first)
	map_data[y][x] = 1
	wall_order_list[0] = (x,y)
	for wall_second in range(1, max_zero_order):
		#print("wall_2 : %d"%wall_second)
		x, y = zero_order_check(map_data, wall_second)
		map_data[y][x] = 1
		wall_order_list[1] = (x,y)
		for wall_third in range(1, max_zero_order):
			#print("wall_3 : %d"%wall_third)
			x, y = zero_order_check(map_data, wall_third)
			#if x == None:
				#print("None Test")
				#map_check(map_data)
				#print("x, y")
			#print(x, y) #test
			map_data[y][x] = 1

			start_x, start_y = zero_order_check(map_data, 1) # 길찾기를 시작할 빈칸의 좌표
			result.append(find_way(map_data))
			#if wall_first == 1 and wall_second == 4 and wall_third == 14:
				#print("aaaaaaaaaaaaa")
				#print(start_x, start_y)
				#map_check(map_data)
				#print(find_way(map_data))

			map_data[y][x] = 0
		map_data[wall_order_list[1][1]][wall_order_list[1][0]] = 0
	map_data[wall_order_list[0][1]][wall_order_list[0][0]] = 0

#print(result)
print(max(result))
print("end")
while 1: continue

'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''