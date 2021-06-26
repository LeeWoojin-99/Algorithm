'''
BOJ 4948
베르트랑 공준
'''

'''
에라토스테네스의 체를 이용하여 풀이
'''

check_prime = [True]*(123456*2+1)

for i in range(2, 123456*2+1):
	if check_prime[i] == True:
		for j in range(i*2, 123456*2+1, i):
			check_prime[j] = False

while 1:
	n = int(input())
	count = 0

	if n == 0: break

	for i in range(n+1, 2*n+1):
		if check_prime[i] == True:
			count += 1
	print(count)
