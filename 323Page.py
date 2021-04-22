'''
323 Page
문자열 압축
realization problem
'''

def solution(s):

	result = []
	ss = '' # 각 단위로 압축한 문자열을 담기 위한 변수

	for i in range(1, len(s)//2 +1):
		# 2 : 문자열을 나눌 수 있는 최소 단위
		# len(s)//2: 문자열을 나눌 수 있는 최대 단위
		#  range 함수에서 '까지'라는 의미로 사용하기 위해서 +1을 해주었다.
		#print("i : %d"%i) # test

		ss = ''
		compression_count = 1 # 압축을 할 횟수를 세기 위한 변수

		for j in range(1, len(s)//i +1):
			# 1 : s[i*(j-1):i*j] 여기서 j-1이 0보다 낮은 수면 안되기 때문에 1부터 시작
			# len(s)//i : 문자열 s를 i개로 나눌 수 있는 최대 횟수
			#print("j : %d"%j) #test

			previous_str = s[i*(j-2):i*(j-1)] if j-2 >= 0 else '' # 이전 문자열
			currunt_str = s[i*(j-1):i*j] # 현재 문자열

			#print("previous_str : %s\ncurrunt_str : %s"%(previous_str, currunt_str)) #test

			if previous_str == currunt_str: # 이전 문자열과 같음
				compression_count += 1 # 압축을 할 횟수를 추가
			else: # 이전 문자열과 다름
				if compression_count > 1: # 1번 이상 압축이 되었다면
					ss += str(compression_count) + previous_str # 기존의 ss + 압축한 횟수 + 압축한 문자열
					compression_count = 1 # 초기화
				else:
					ss += previous_str # 압축이 되지 않은 채 문자열 추가

		# 마지막 문자열을 추가시키기 위해서
		# j for문에서 ss += currunt_str로 하고 이 조건문을 넣지 않는다면 압축이 이상하게 됨
		if compression_count > 1:
			ss += str(compression_count) + currunt_str
			compression_count = 1
		else:
			ss += currunt_str

		#print(i*(j-1)) #test
		#print(len(s)-1) #test
		ss += s[i*j:] if len(s)-1 > i*(j-1) else '' # 나머지 문자열 처리

		print(ss) #test
		result.append((len(ss), i))
		#print() #test

	#print(result)

	return min(result, key = lambda x: x[0])[0]

print(solution('aabbaccc'))