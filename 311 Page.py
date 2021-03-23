'''
311 Page
모험가 길드
Greedy Algorithm Problem

문제 설명
한 마을에 모험가 N명 존재
공포도가 X인 모험가는 반드시 X명 이상을
 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있느 그룹 수의 최댓값을 구하는 프로그램을 작성

입력 조건
첫째 줄 입력 : 모험가의 수 N
둘째 줄 입력 : 각 모험가의 공포도 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분
출력 조건
여행을 떠날 수 있는 그룹 수의 최댓값을 출력

입력 예시
5
2 3 1 2 2

'''

n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)
count = 0
for i in arr:
    for j in range(i):
        arr.pop(0)
        if arr == []:
            break
    count += 1
print(count)