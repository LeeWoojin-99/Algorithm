'''
220 Page
개미 전사

문제 설명
식량 창고는 일직선으로 이어져 있다.
서로 인접한 식량 창고가 공격받으면 들킨다.
최소한 한 칸 잇아 떨어진 식량 창고를 약탈해야 한다.
최대한 많은 식량을 얻기를 원한다.
식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하시오.

입력 조건
첫째 줄 : 식량창고의 개수 N이 주어진다.
둘째 줄 : 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다.

출력 조건
개미 전사가 얻을 수 있는 식량의 최댓값을 출력
'''

''' 입력 예시
4
1 3 1 5
'''

n = int(input())
arr = list(map(int, input().split()))
print("\nInput Data Checking\nn : {}\narr : {}\n".format(n, arr))

d = [0]*100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+arr[i])
print(d[n-1])
