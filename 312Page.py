'''
312 Page
곱하기 혹은 더하기
Greedy Algorithm Problem
'''
''' 문제 설명
각 자리가 숫자로만 이루어진 문자열 S
숫자 사이에 곱하기 또는 더하기 연산을 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램 작성

모든 연산은 왼쪽에서부터 순서대로 이루어진다.
'''
''' 문제 풀이
result1 더하기
result2 곱하기
연산 후 비교하여 더 큰 값을 선택하는 과정을 반복
'''
n = str(input())
result1 = 0
result2 = 0

for i in range(len(n)):
	result1 = result1 + int(n[i])
	result2 = result2 * int(n[i])
	if result1 > result2:
		result2 = result1
	else:
		result1 = result2
print(result1)


'''
02984
'''
'''
567
'''