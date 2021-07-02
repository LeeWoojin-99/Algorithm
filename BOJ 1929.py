'''
BOJ 1929
소수 구하기
'''

'''
에라토스테네스의 체를 이용하여 풀이
'''

m, n = map(int, input().split())

check = [True]*(n+1)
# index 0 ~ n
# False : 소수가 아니다.
# True : 소수가 맞다.

for i in range(2, n+1):
	# 2 ~ n
	if check[i] == True: # i가 소수가 맞다면

		if i >= m: print(i) # i가 m이상의 숫자라면 출력

		for j in range(i*2, n+1, i):
			# i*2 ~ n
			# i씩 증가
			# i의 배수는 소수가 무조건 아니다.
			check[j] = False