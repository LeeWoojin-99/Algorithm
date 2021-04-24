'''
327 Page
뱀
realization problem
'''
import heapq

def arr_check(arr):
	for i in range(1, len(arr)):
		for j in range(1, len(arr)):
			print(arr[i][j], end=' ')
		print()

# 보드의 크기 n x n
n = int(input())
n_arr = [[0]*(n+1) for _ in range(n+1)]
# 사과의 개수
# 사과의 위치
k = int(input())
k_arr = []
for _ in range(k):
	y, x = map(int, input().split())
	k_arr.append((x,y))
# l : 뱀의 방향 변환 횟수
# 방향이 바뀌는 시간과 방향
l = int(input())
l_dic = {}
for _ in range(l):
	x, y = input().split()
	# x : 경과한 시간
	# y : 방향 명령
	l_dic[int(x)] = y

# 뱀은 맨 위 맨 좌측에 위치하고 오른쪽을 바라본다
# 1초에 한 칸씩 움직인다
# 벽 또는 자기 자신과 부딪히면 게임이 끝

break_point = False # 벽이나 자신의 몸에 닿은 경우
result = 0 # 경과된 시간
x, y = 1, 1 # 현재 위치 좌표
direction = 1
# 0 right, 1 down, 2 left, 3 up
tail = [] # 꼬리를 찾기 위한 몸 데이터를 저장하는 리스트
heapq.heappush(tail, (1,1))
n_arr[1][1] = 1
#print("%d초 경과\n좌표\nx : %d\ny : %d\n방향 : %d\n"%(result, x, y, direction)) # test
while 1:
		
	result += 1 # 시간 1초 진행

	#print("%d초 경과"%result) #test

	# 방향에 따라서 다음 위치 좌표 설정
	if direction == 1: # right
		x += 1
	elif direction == 2: # down
		y += 1
	elif direction == 3: # left
		x -= 1
	elif direction == 4: # up
		y -= 1

	#print("좌표\nx : %d\ny : %d"%(x, y)) # test

	# 설정된 다음 위치 좌표가 안전한지 확인
	if 1 <= x <= n and 1 <= y <= n and n_arr[y][x] == 0: # 안전한 조건
		None
	else: # 안전하지 않은 조건
		break # while문을 탈출

	n_arr[y][x] = 1 # 전진
	#arr_check(n_arr)
	heapq.heappush(tail, (x,y)) # 몸 데이터 최신화

	# 전진한 곳에 사과가 없다면 꼬리가 수축
	if not (x,y) in k_arr: # 사과가 없다면
		tail_x, tail_y = heapq.heappop(tail) # 꼬리가 어디인지 priority queue를 통해 찾기
		n_arr[tail_y][tail_x] = 0 # 꼬리 수축
	else:
		#print("사과 먹음") # test
		k_arr.remove((x,y))

	# 방향 전환을 해야 하는지
	if result in l_dic: # 현재 경과된 시간에 방향 전환을 해야하는지
		if l_dic[result] == 'D':
			direction += 1
			if direction > 4:
				direction = 0
		elif l_dic[result] == 'L':
			direction -= 1
			if direction < 1:
				direction = 4

	#print("방향 : %d"%direction) # test
	#arr_check(n_arr) # test
	#print() # test

print("result : %d"%result)

'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
'''
'''
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
'''
'''
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
'''