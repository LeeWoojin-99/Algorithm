'''
346 Page
괄호 변환
DFS/BFS Algorithm Problem
'''


def rightness_check(s):
	# 올바른 문자열인지 판별하는 함수
	left = 0
	right = 0

	for i in s:
		if i == '(':
			left += 1
		elif i == ')':
			if left - right == 0: # '('가 없는데 ')'가 나타난 경우
				return False # 올바르지 않은 괄호 문자열로 판명
			right -= 1

	return True

def solution(w):
	result = '' # 결과값이 담길 공간
	
	u = ''
	v = ''
	# 문자열 w가 u, v로 분리되어 담길 예정

	if w == "": return "" # 문자열 w가 빈 문자열이라면 빈 문자열을 반환

	left = 0 # (
	right = 0 # )
	# right, left : 균형잡힌 괄호 문자열을 찾아내기 위한 변수
	u_balance = False # 균형잡힌 괄호 문자열 u가 분리되었는지 확인하는 변수

	# 문자열 w를 u, v로 분리하는 과정
	for i in w:
		#print(i) #TEST
		if u_balance == True:
			#print("True") #TEST
			v += i
		elif u_balance == False:
			#print("False") #TEST
			if i == '(':
				left += 1
			elif i == ')':
				right += 1
			u += i
		if left - right == 0:
			u_balance = True

	# 균형잡힌 괄호 문자열 u가 올바른 괄호 문자열인지 판별
	u_rightness = rightness_check(u)

	if u_rightness == True: # 문자열 u가 올바른 문자열 이라면 문자열 v에 대해 1단계부터 다시 수행
		result += u # u는 변환이 완료되었으므로 결과값에 추가
		result += solution(v) # 수행한 결과 문자열을 u에 이어 붙인 후 반환
	else: # 문자열 u가 올바른 문자열이 아니라면
		result += '('
		result += solution(v)
		result += ')'
		u = u[1:len(u)-1]
		for i in u:
			if i == '(':
				result += ')'
			elif i == ')':
				result += '('

	return result # 변환이 완료된 올바른 괄호 문자열을 반환

print(solution("()"))
print(solution("()))((()"))
print(solution(""))
print(solution(")("))