#182 Page
#두 배열의 원소 교체

''' 문제 설명
첫 번째 줄 입력 : 두 배열의 크기 N, 바꿔치기 횟수 K가 공백으로 구분되어 입력
2~3 번째 줄 입력 : 배열의 원소값

2번째 줄의 입력으로 받은 배열 원소값들의 합이 최대값이 되도록
K번 3번째 줄의 입력으로 받은 배열의 원소와 바꿔치기를 할 수 있다.
최대값을 구하시오.
'''
''' 문제 풀이
K값만큼 두 배열에서 최소값, 최대값을 구한다.
최대값이 되어야 하는 배열이 최소값이다.
'''

n, k = list(map(int, input().split()))
arr = []
for i in range(2):
    arr.append(list(map(int, input().split())))
for i in range(2):
    arr[i] = sorted(arr[i])
arr[1].reverse()
#arr[0] 오름차순, arr[1] 내림차순
arrMax, arrMin = 0, 0
count = 0
while count != k:
    if arr[0][arrMin]<arr[1][arrMax]:
        arr[0][arrMin], arr[1][arrMax] = arr[1][arrMax], arr[0][arrMin]
        arrMax += 1
        count += 1
    else:
        break
print(sum(arr[0]))

'''
5 3
1 2 5 4 3
5 5 6 6 3
'''