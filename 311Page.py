'''
311 Page
모험가 길드
Greedy Algorithm Problem
'''
'''
 문제 설명
모험가 N명
각 모험가의 '공포도'가 존재
공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최대값을 구하라.

 입력 조건
첫째 줄 : 모험가의 수 N
둘째 줄 : 각 모험가의 공포도 값을 N이하의 자연수로 주어지며 각 자연수는 공백으로 구분하여 입력

 출력 조건
여행을 떠날 수 있는 그룹 수의 최대값을 출력
'''

n = int(input())
x = list(map(int, input().split()))
count = 0
group = 0
x.sort()

for i in x:
	count += 1
	#현재 그룹에 모험가를 추가
	if count == i: #그룹을 완성시킬 수 있는 조건
		if count > i:
			print(count, i)
		#그룹을 완성
		group += 1 #완성된 그룹이 생겼기 때문에 그룹의 개수 증가
		count = 0 #새로운 그룹의 인원 수를 초기화
print(group)
'''
5
2 3 1 2 2
'''