'''
329 Page
기둥과 보 설치
realization problem
'''
def zero_check(arr, n, answer):
	# 기둥의 동작을 수행하는 함수
	# 기둥은 아래에 [바닥/보의 한쪽 끝 부분/다른 기둥]이 있어야 한다.
	x = arr[0]
	y = arr[1]


	if arr[3] == 0: # 삭제
		#if arr == [2, 0, 0, 0]: print("test\n{}".format(answer))
		#print("기둥을 삭제하려고 한다.") #test
		# 기둥을 삭제하려면 위에 기둥 또는 보가 설치되어 있는지 확인
		if [x, y+1, 0] in answer:
			# 위에 기둥이 있는 경우
			#print("기둥 삭제 실패") #test
			# 삭제하여 구조물 규칙에 어긋난다면 None을 리턴
			return None 
		elif [x, y+1, 1] in answer:
			# 위에 보가 있는 경우
			if [x-1, y+1, 1] and [x+1, y+1, 1]:
				#print("기둥 삭제 성공") #test
				answer.remove([x, y, 0])
			else:
				#print("기둥 삭제 실패") #test
				return None
		else:
			#print("기둥 삭제 성공") #test
			answer.remove([x, y, 0]) # 기둥을 삭제

	else: # 설치
		# 설치
		# 기둥을 설치하려는 (x, y) 좌표에서 밑에 보가 있는지 확인하려면 (x-1, y) 좌표를 확인해야 한다.
		# y 좌표가 0이라면 바닥
		#print("기둥을 설치하려고 한다.") #test
		#if arr == [5, 1, 0, 1]: print("test\n{}".format(answer))
		
		if y != n and ([x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer or y == 0):
			# 바닥인 경우
			# 보가 있는 경우 : [x, y, 1] or [x-1, y, 1]
			# 밑에 기둥이 있는 경우
			#print("기둥 설치 성공") #test
			answer.append([x, y, 0])
		else:
			#print("기둥 설치 실패") #test
			return None

	return answer

	# 삭제 또는 설치를 수행 후 알맞는지 확인
	# 알맞다면 결과에 추가한 값을 반환, 알맞지 않다면 None 반환

def one_check(arr, n, answer):
	# 보의 동작을 수행하는 함수
	# 보는 아래에 기둥이 있는지 확인 : (x, y-1)에 기둥이 존재하는지
	# 보는 왼쪽과 오른쪽에 둘 다 보가 있는지 확인
	x = arr[0]
	y = arr[1]

	if arr[3] == 1: # 설치
		#print("보를 설치하려고 한다.") #test
		if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
			#print("보 설치 성공") #test
			# 밑에 기둥이 있는 경우 설치
			answer.append([x, y, 1])
		elif 0 <= x <= n-2:
			# x좌표가 보를 설치할 수 있는 좌표인지
			if [x-1, y, 1] in answer and [x+1, y, 1] in answer:
				#print("보 설치 성공") #test
				answer.append([x, y, 1])
			else:
				#print("보 설치 실패")
				return None
		else:
			#print("보 설치 실패") #test
			return None
	else: # 삭제
		# 보를 삭제했을 때 문제되는 조건
		#  1. 보가 있어야만 기둥이 세워지는 경우 : (x, y, 0) or (x+1, y, 0)
		#  2. 보가 있어야만 보가 존재할 수 있는 경우 : ((x-2, y, 1) and (x-1, y, 1)) +의 경우도
		#print("보를 삭제하려고 한다.") #test
		if [x, y, 0] in answer or [x+1, y, 0] in answer:
			print("보 삭제 실패") #test
			# 기둥 확인
			return None
		elif [x-1, y, 1] in answer or answer[x-2, y, 1] in answer:
			# 왼쪽 보 확인
			#print("보 삭제 실패") #test
			return None
		elif [x-1, y, 1] in answer or answer[x-2, y, 1] in answer:
			# 오른쪽 보 확인
			#print("보 삭제 실패") #test
			return None
		else:
			#print("보 삭제 성공") #test
			answer.remove([x, y, 1])

	return answer



def solution(n, build_frame):
	answer = []
	result = []
	#print(build_frame) #test

	# 기둥인지 보인지 확인
	for i in build_frame:
		#print() #test
		#print(i) #test
		if i[2] == 0:
			result = zero_check(i, n, answer)
			if result != None:
				answer = result
		else:
			result = one_check(i, n, answer)
			if result != None:
				answer = result

	# answer.append 하는 식으로 결과값을 추가
	#print()

	answer.sort()

	return answer

# x y a b : (x,y)에 a를 b를 수행
# a : 0은 기둥, 1은 보
# b : 0은 삭제, 1은 설치

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
#print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))

# return : [x, y, a] : (x,y)에 a가 존재
# x,y 좌표가 모두 같은 경우 기둥이 보보다 앞에 온다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제
#  왼쪽에서 오른쪽, 아래에서 위쪽

'''
[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
'''