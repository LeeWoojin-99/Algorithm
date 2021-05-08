'''
연산자 끼워 넣기
'''
'''
N개의 수열

사칙연산의 개수 : + - * %
연산은 무조건 앞에서 뒤로

음수 나누기 양수
음수를 양수로 바꾼 후 나눈 몫을 음수로 바꾼 값이 결과
'''
'''
가장 크거나 가장 작은 값을 계속해서 선택해 나간다.
아꼈다가 더 좋은 결과를 도출해낼 수도 있는가 ?

3
3 4 5
1 0 1 0
result
35
17

3 4
+ : 7
* : 12
'''

from itertools import permutations

def divide(a, b):
	if a == 0 or b == 0:
		return 0
	elif a < 0:
		return abs(a) // b * -1
	else:
		return a // b

def operate_func(a, b, f_operator):
	if f_operator == 0:
		return a + b
	elif f_operator == 1:
		return a - b
	elif f_operator == 2:
		return a * b
	elif f_operator == 3:
		return divide(a, b)

n = int(input())
# 수열의 숫자 개수

arr = list(map(int, input().split()))
# 수열

remainning_operator = list(map(int, input().split()))
# + - * / 순서

# 연산의 모든 경우를 구하는 과정
operator = []
for i in range(4):
	# 사용할 수 있는 연산들을 이어붙여서 리스트로 만드는 과정
	# ooperator 리스트는 permuatations 함수의 인수값으로 쓰일 예정이다.
	for j in range(remainning_operator[i]):
		operator.append(i)
#print(operator) #TEST
operator_cases = list(permutations(operator, len(operator))) # 연산의 경우들이 담길 공간

result = [arr[0] for i in range(len(operator_cases))] # 각 연산 경우에 대한 연산 결과가 담길 공간
for i in range(1, len(arr)):
	# 연산의 개수만큼 반복하는 for문
	# 연산을 왼쪽부터 오른쪽으로 차례대로 수행
	# i번째 연산
	for oper in range(len(result)):
		# 연산의 경우의 수만큼 반복하는 for문
		# i번째 연산을 각 경우의 수마다 수행
		# oper : oper+1번째 경우
		result[oper] = operate_func(result[oper], arr[i], operator_cases[oper][i-1])
		# result[oper] : 현재까지 연산이 진행되어 있는 결과
		#  경우마다 다른 결과값
		# arr[i] : 이번에 연산을 할 숫자
		# operator_cases[oper][i-1] : 이번 차례에 해야 할 연산

print(max(result))
print(min(result))

'''
2
5 6
0 0 1 0
result
30
30

3
3 4 5
1 0 1 0
result
35
17

6
1 2 3 4 5 6
2 1 1 1
54
-24
'''