from itertools import permutations
# 경우의 수를 구할 수 있는 라이브러리 permutations


def solution(n, weak, dist):
	# 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
	length = len(weak)
	for i in range(length):
		weak.append(weak[i]+n)
	#print("weak : {}".format(weak)) #TEST

	answer = len(dist) + 1
	# 왜 +1을 해준 것일까 ?
	# 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist)+1로 초기화
	
	for start in range(length):
	# 0부터 length-1까지의 위치를 각각 시작점으로 설정
		#print("start : %d"%start) #TEST

		for friends in list(permutations(dist, len(dist))):
			# 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
			#print("friends : {}".format(friends)) #TEST

			count = 1 # 투입할 친구의 수
			position = weak[start] + friends[count-1] # 투입된 친구가 시작 지점인 weak[start]에서부터 점검할 수 있는 최대 거리

			for index in range(start, start+length): # 시작점부터 모든 취약 지점을 확인
				#print("index : %d"%index) #TEST
				#print("now position : %d"%position) #TEST
				#print("weak[index] : %d"%weak[index]) #TEST #TEST

				if position < weak[index]:
				# position에서 점검하고 있는 사람이 weak[index] 지점까지는 점검하지 못함
					#print("position < weak[index]\n%d < %d"%(position, weak[index])) #TEST
					count += 1 # 새로운 친구를 투입

					if count > len(dist): # 인원 부족
						#print("인원 부족") #TEST
						break

					position = weak[index] + friends[count-1]
					# count += 1로 바뀐 새로운 친구 friends[count-1]이 weak[index]에서부터 점검을 시작하여 점검할 수 있는 최대 거리
					#print("new position : %d"%position) #TEST
				#print() #TEST
			answer = min(answer, count)
			#print("\n") #TEST

	if answer > len(dist): return -1 # 인원 초과

	return answer
    

print("결과값 : %d"%solution(12, [1,5,6,10], [3,4]))
#print(solution(12, [1,3,4,9,10], [3,5,7]))

'''
n : 외벽의 길이
weak : 취약 지점의 위치가 담긴 배열
dist : 각 친구가 1시간 동안 이동할 수 있는 거리

취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 구하시오.
'''
'''
1 3 4 9 10 13 15 16 21 22
1 3 4 9 10  1  3  4  9 10
'''