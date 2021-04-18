'''
314 Page
만들 수 없는 금액
Greedy Algorithm Problem
'''
'''
 입력 조건
첫째 줄 : 동전의 개수를 나타내는 양의 정수 N
둘째 줄 : 각 동전의 화폐 단위를 나타내는 N개의 자연수. 각 자연수는 공백으로 구분.

 출력 조건
주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력
'''
'''
현재 금액을 가지고 있는 동전들로 어떻게 구현할까 ?
'''

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1

for x in arr:
	if target < x: break
	#target 금액을 구현할 수 있는지 확인
	target += x
	#위의 문장을 거친 상태에서 진행된 arr의 원소만으로
	# target-1 까지 구현할 수 있다.

print(target)

'''
5
3 2 1 1 9
'''
'''
4
1 1 3 5
'''