'''
344 Page
경쟁적 전염
DFS/BFS Algorithm Problem
'''
'''
virous_data[바이러스 k].append((x, y))
나중에 바이러스가 증식할 때
virous_data[바이러스 k]에서 불러온 x, y에서 한칸씩 증가시킬 예정
'''

def map_data_check(map_data):
	print("Map Data Check Function")
	for y in range(n):
		for x in range(n):
			print(map_data[y][x], end=' ')
		print()


n, k = map(int,input().split())
# n : 맵의 크기 n x n
# k : 바이러스의 종류가 k가지
map_data = []
# 맵 정보가 담기는 map_data
virous_data = [[] for _ in range(k+1)]
# K번 바이러스의 정보를 꺼내올 때 인덱스로 접근하기 쉽게하기 위해서 range(k+1)
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 위쪽부터 시계 방향의 방향들

# 맵 정보 입력
for y in range(n):
	map_data.append(list(map(int,input().split())))
	for x in range(n):
		if map_data[y][x] != 0: # (x, y) 좌표에 바이러스가 있다면
			virous_data[map_data[y][x]].append((x, y))
			# 바이러스 정보 입력

s, x, y = map(int,input().split())
result_point = (x, y)

'''print("\nInput Data Check\nInput Data Check\n") #TEST
map_data_check(map_data) #TEST
print("virous_data : {}".format(virous_data)) #TEST
print("s : {}\nresult_point = {}".format(s, result_point)) #TEST
print("\nInput Data Check\nInput Data Check\n") #TEST'''

for for_s in range(s): # s초 후의 데이터를 얻기 위해서 1초씩 진행
	#print("\n\n\n%d초 진행. 바이러스 증식 예정"%(for_s+1)) #TEST
	for virous_number in range(1, k+1):	# 1~k번까지의 바이러스가 증식
		#print("%d번 바이러스 증식"%virous_number) #TEST
		new_virous = [] # virous_number번 바이러스가 증식되어 새롭게 바이러스가 들어선 좌표
		for x, y in virous_data[virous_number]: # virous_number번 바이러스를 증식
			#print("(%d, %d) 좌표의 %d번 바이러스 증식"%(x, y, virous_number)) #TEST
			# virous_data[virous_number] : (x, y) 형태로 저장되어 있는 해당 번호의 바이러스의 위치 정보

			for direction_x, direction_y in direction:
				x += direction_x
				y += direction_y

				#print(x, y) #TEST
				if 0 <= x <= n-1 and 0 <= y <= n-1 and map_data[y][x] == 0:
					#print("증식 가능") #TEST
					# not(0 <= x <= n-1) : 맵의 한계를 벗어나지 않는지 확인
					# map_data[y][x] == 0 : 이동한 좌표가 비어있는 좌표인지 확인
					map_data[y][x] = virous_number
					new_virous.append((x, y))

				x -= direction_x
				y -= direction_y

		for i in new_virous: virous_data[virous_number].append(i)
		#print("증식된 {}번 바이러스 상황 : {}".format(virous_number, virous_data[virous_number])) #TEST

	#print("%d초 진행된 맵 진행 상황"%(for_s+1)) #TEST
	#map_data_check(map_data) #TEST

x, y = result_point
print("\n%d행 %d열 : "%(x, y), end='')
print(map_data[x-1][y-1])



'''
3 3
1 0 2
0 0 0
3 0 0
1 2 2
n, k
map data
s, x, y
'''
'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2
'''