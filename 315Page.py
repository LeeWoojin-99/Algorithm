'''
315 Page
볼링공 고르기
Greedy Algorithm Problem
'''
'''
 문제 설명
A, B 두 사람이 볼링을 치고 있습니다.
두 사람은 서로 무게가 다른 볼링공을 고르려고 한다.
볼링공은 N개 존재
볼링공의 무게는 1부터 M까지의 자연수 형태로 존재
두 사람이 공을 고르는 경우의 수를 구하시오

 입력 조건
첫째 줄 : 볼링공의 개수 N, 공의 최대 무게 M
둘째 줄 : 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어진다.

 출력 조건
두 사람이 볼링공을 고르는 경우의 수를 출력
'''

n, m = map(int, input().split())
k = list(map(int, input().split()))
count = 0

for i in range(n-1):
	for j in range(i+1, n):
		if k[i] != k[j]:
			count += 1

print(count)

'''
5 3
1 3 2 3 2
'''
'''
8 5
1 5 4 3 2 4 5 2
'''


