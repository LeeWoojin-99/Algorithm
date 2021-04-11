'''
298 Page
팀 결성
Graph Algorithm Problem
'''
''' 문제 설명
학생들에게 0~N번까지의 번호를 부여
처음에는 모든 학생이 서로 다른 팀
선생님께서 '팀 합치기', '같은 팀 여부 확인'의 연산을 할 수 있다.
연산이 모두 이루어졌을 때 '같은 팀 여부 확인' 연산에 대한 결과를 구하시오.
'''
''' 입력 및 출력 조건
첫째 줄 : 번호의 개수에 관여하는 N, 연산의 횟수 M
다음 M개의 줄 :
 '팁 합치기' 연산 : 0 a b : a번 학생의 팀과 b번 학생의 팀을 합치기
 '같은 팀 여부 확인' 연산 : 1 a b : a번 학생과 b번 학생이 같은 팀인지 확인
'''
''' 문제 풀이
서로소 집합 자료구조 알고리즘의 find, union 연산 구현.
'''

def dss_find(parent, x):
	if parent[x] != x:
		parent[x] = dss_find(parent, parent[x])
	return parent[x]

def dss_union(parent, x, y):
	#dss : disjoint sets structure : 서로소 집합 자료구조
	x = dss_find(parent, x)
	y = dss_find(parent, y)
	if x < y:
		parent[y] = x
	else:
		parent[x] = y

node, edge = map(int, input().split())
parent = [0]*(node+1)

for i in range(1, node+1):
	parent[i] = i

for i in range(edge):
	op, x, y = map(int, input().split())

	if op == 1:
		dss_union(parent, x, y)
	elif op == 0:
		if dss_find(parent, x) == dss_find(parent, y):
			print("YES")
		else:
			print("NO")
	else:
		print("input data error")

''' input data
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''