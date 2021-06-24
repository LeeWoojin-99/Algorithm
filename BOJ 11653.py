'''
BOJ 11653
소인수분해
'''

n = int(input())
count = 2

while n != 1:
	if n%count == 0: # n을 count로 분해할 수 있는 경우
		print(count)
		n //= count
	else: # n을 count로 분해할 수 없는 경우
		count += 1