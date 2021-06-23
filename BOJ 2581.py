'''
BOJ 2581 소수
소수 : 1과 자기 자신을 제외하고는 나누어 떨어지지 않는 수
1은 소수가 아니다.
'''

m = int(input())
n = int(input())

check = False
result = 0
min_result = 0

if n > 1:
	for i in range(m, n+1):
		# range(m, n+1) = m ~ n

		check = False

		for j in range(2, i):
			if i % j == 0: # i가 소수가 아닌 경우
				check = True
				break

		if check == False and i != 1: # i가 소수인 경우
			if min_result == 0 and i > 1:	min_result = i
			result += i

if result == 0:
	print("-1")
else:
	print(result)
	print(min_result)