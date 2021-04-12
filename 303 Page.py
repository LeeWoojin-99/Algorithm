'''
303 Page
커리 큘럼
Topology Sort Algorithm Problem

입력 조건
첫째 줄 : 강의의 수 N
다음 N개의 줄 : 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호
N개의 줄의 각 줄은 -1로 끝난다.
각 강의 번호는 1부터 N까지로 구성

출력 조건
N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력
'''
'''
1.
선행 강의가 없는지 확인.
for문으로 indegree를 확인. indegree가 0이라면 queue에 넣기.

2.
선행 강의가 없는 강의를 수강 완료.
queue에서 꺼낸 강의는 수강 완료된 강의.
precedence를 확인하여 수강 완료된 강의를 선행으로 해야하는 강의의 indegree에서 1을 뺄셈.
for문으로 indegree를 확인. indegree가 0이라면 queue에 넣기.
제거할 때 목록을 지니는 강의의 시간에 제거되는 강의의 시간만큼 덧셈

1, 2번 동작을 반복
모두 수강 완료된 강의가 됬을 때 종료
'''
from collections import deque

node = int(input())
precedence = [[] for i in range(node+1)] #자기 자신을 선행으로 가지는 강의들이 무엇인지
time = [0]*(node+1) #강의 시간
indegree = [0]*(node+1) #진입 차수
queue = deque() #진입 차수가 0인 것을 넣을 큐

for i in range(1, node+1):
	input_data = list(map(int, input().split()))
	time[i] = input_data[0]
	for j in range(1, len(input_data)-1):
		precedence[input_data[j]].append(i) #i번 강의는 j번 강의를 선행 수강이 필요
		indegree[i] += 1 #진입 차수 카운트
result_time = time[:] #선행까지 합쳐서 걸리게 되는 시간 결과값

for i in range(1, node+1): #진입 차수가 0인 강의 번호를 queue에 삽입
	if indegree[i] == 0:
		queue.append(i)

while queue:
	now = queue.popleft()

	for i in precedence[now]: #now번 강의를 필요로 하는 i번 강의
		indegree[i] -= 1 #now번 강의를 수강했으니 진입 차수 뺄셈하여 선행 강의를 개수 변경
		result_time[i] = result_time[now]+time[i] #now번 강의를 수강한 시간을 반영
		#어차피 자신에게 제일 가까운 선행 강의의 시간에 맞춰서 결과값이 달라지게 때문에
		#result_time[now]를 사용하였다.
		if indegree[i] == 0: #수강 후에 선행 강의가 없는 강의를 queue에 삽입
			queue.append(i)

print("result : ", end = '')
for i in range(1, len(result_time)):
	print(result_time[i], end=' ')

'''
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
'''