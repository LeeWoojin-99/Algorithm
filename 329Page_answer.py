def possible(answer):
	for x, y, stuff in answer:

		if stuff == 0: # 기둥
			if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
				# y == 0 : 바닥의 위
				# [x-1, y, 1], [x, y, 1] : 보의 한쪽 끝의 위
				# [x, y-1, 0] : 다른 기둥의 위
				continue
			return False # 조건에 부합하지 못한다면 False 반환

		elif stuff == 1:
			if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
				# [x, y-1, 0], [x+1, y-1, 0] : 한쪽 끝 부분이 기둥의 위
				# [x-1, y, 1] and [x+1, y, 1] : 양쪽 끝 부분이 다른 보와 동시에 연결
				continue
			return False # 조건에 부합하지 못한다면 False 반환
			
	return True

def solution(n, build_frame):
	answer = []

	for frame in build_frame:

		x, y, stuff, operate = frame
		# x, y : 좌표
		# stuff : 구조물
		# operate : 동작

		if operate == 0: # 삭제
			# 삭제한 후에 가능한 구조물인지 확인
			answer.remove([x, y, stuff])
			if not possible(answer):
				answer.append([x, y, stuff])

		if operate == 1: # 설치
			# 설치한 후에 가능한 구조물인지 확인
			answer.append([x, y, stuff])
			if not possible(answer):
				answer.remove([x, y, stuff])

	return sorted(answer)
