'''
BOJ 9020 골드바흐의 추측
'''

check_prime = [True]*(123456*2+1)
# True : 소수가 맞다.
# False : 소수가 아니다.
check_prime[0] = False
check_prime[1] = False

for i in range(2, 123456*2+1):
	if check_prime[i] == True: # i가 소수가 맞다면
		for j in range(i*2, 123456*2+1, i):
			check_prime[j] = False # 소수 i의 배수인 j는 모두 소수가 아니다.

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n//2, 1, -1):
        if check_prime[n - j] == True and check_prime[j] == True:
            print(j, n - j)
            break