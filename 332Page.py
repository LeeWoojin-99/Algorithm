'''
332 Page
치킨 배달
realization problem
'''
import heapq

def sum_min_chiken_load(house, m_check_chiken):
	# 집의 정보를 담고있는 house
	# m개의 치킨집의 정보를 담고잇는 m_check_chiken
	# check_chiken에 저장되어 있는 존재하는 m개의 치킨집들 까지의
	#  치킨 거리들의 최소값을 각 집마다 구하여 그 최소값들의 합을 구하는 함수
	#print("sum_min_chiken_load func 호출") #test
	#print(m_check_chiken)

	min_chiken_load = 0 # 치킨 거리의 최소값의 합을 저장하는 변수
	for i in house:
	# 치킨 거리의 최소값을 각 집마다 구하기 위해서 iterable로 house를 사용
		queue = [] # 우선순위 큐가 될 공간
		for j in m_check_chiken:
		# 치킨 거리의 최소값을 구하기 위해서 iterable로 존재하는 m개의 치킨집들을 요소로 가지고 있는 check_chiken을 사용
			#print(i, j, (abs(i[0]-j[0]) + abs(i[1]-j[1])))
			heapq.heappush(queue, ( (abs(i[0]-j[0]) + abs(i[1]-j[1])) )) # 최소 치킨 거리를 구하기 위해서 우선순위 큐를 사용
		#print()
		min_chiken_load += heapq.heappop(queue) # 현재 집 i의 최소 치킨 거리를 결과값에 추가

	return min_chiken_load


n, m = map(int, input().split())
arr = [[0]*(n) for _ in range(n)]

queue = [] # 치킨 거리가 저장될 공간
house = [] # 집의 위치 정보
# 집은 1
chiken = [] # 치킨집의 위치 정보
# 치킨집은 2
result = [] # 결과값이 담길 공간

for y in range(n):
	input_data = list(map(int, input().split()))

	for x in range(n):
		arr[x][y] = input_data[x]

		if input_data[x] == 1: # 집의 위치 정보를 저장
			house.append((x,y))
		elif input_data[x] == 2: # 치킨집의 위치 정보를 저장
			chiken.append((x,y))

'''print("\narr 입력 확인") #test
for y in range(n): #test
	for x in range(n):
		print(arr[x][y], end=' ')
	print()
print()'''

#print("house : {}\nchiken : {}\n".format(house, chiken)) #test

count = m-1
#print("len(chiken) - (m-1) : %d"%(len(chiken) - count)) #test
#print("len(chiken) : %d\nm-1 : %d\n"%(len(chiken), m-1)) #test

def for_chiken(chiken_index, start):
	# 치킨집들 중에서 m개의 치킨집으로 구성할 수 있는 경우의 수를 구하는 함수
	# 재귀적으로 호출
	# chiken_index : 치킨집의 위치 정보가 담긴 chiken에 접근할 때 쓰일 index값이 담긴 리스트
	# chiken_index에 m개의 요소값이 담길 예정

	#print("for_chiken func 호출") #test
	#print("chiken_index : {}".format(chiken_index)) #test

	for i in range(start, len(chiken) - (m - len(chiken_index)) +1):
		# m - len(chiken_index) : m개의 치킨집까지 남은 치킨집의 개수
		# +1 : 예시로 알아보는 것이 더 편할듯하다.
		#  ex) 1 2 3 치킨집이 있다. 이 치킨집들의 2개의 치킨집으로 구성할 수 있는 경우의 수를 구할 때
		#  2개의 치킨집 중에 첫 번째 치킨집은 전체 치킨집 개수 3에서 m인 2를 뺀 1에서 +1을 더한 2까지 반복한다.
		#  첫 번째 치킨집은 1부터 2까지 반복하고한다.
		#  1 2, 1 3, 2 3 이렇게 세 가지의 경우의 수를 구할 수 있다.
		#print("추가될 치킨집 i : %d"%i) #test
		
		chiken_index.append(i) # 현재 치킨집을 추가
		#print("chiken_index : {}".format(chiken_index)) #test

		if len(chiken_index) < m: # 재귀적 호출의 종료 조건
			for_chiken(chiken_index, i+1)

		if len(chiken_index) == m:
		# m개만큼 모인 치킨집
		# 모아진 m개의 치킨집에 대한 모든 집의 치킨 거리의 합을 구하면 된다.
			#print("m개의 치킨집 완성") #test
			chiken_check = []
			for i in chiken_index:
				chiken_check.append(chiken[i])
			result.append(sum_min_chiken_load(house, chiken_check))
			#print(result)

		chiken_index.pop()
		# 다른 치킨집을 추가하기 위해서 제거
		# 한 for문에서 한 치킨집만 추가된다.

	#print() #test

for_chiken([], 0)

print("\n결과값 : %d"%min(result))


'''
치킨집의 위치를 튜플 형태로 저장
집의 위치를 튜플 형태로 저장

m개의 치킨집을 남긴다고 할 때, 모든 집의 치킨 거리의 합의 최소값을 구해야 한다.

치킨집을 m개 남기는 경우 모든 경우의 수를 구하는 알고리즘
치킨집의 개수중에서 m개로 구성할 수 있는 경우의 수를 구하는 알고리즘
ex) 5개 중에서 2개로 구성할 수 있는 경우의 수
0 ~ (len(chiken) - m-1)


남은 치킨집에 모든 집의 치킨 거리의 합을 구하는 알고리즘
'''
'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

result : 5
'''
'''
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

result : 10
'''
'''
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

result : 11
'''