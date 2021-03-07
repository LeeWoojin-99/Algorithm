'''
BOJ 1978
소수 찾기
'''
'''
첫번째 줄 입력 : N
N은 100이하
두번째 줄 입력 : N개의 수
N개의 수는 1,000 이하의 자연수
주어진 수들 중 소수의 개수를 출력한다.
소수란 1을 제외하고 자신으로밖에 나누어지지 않는 수이다.
'''

N = int(input())
count = 0
result = []
arr = list(map(int, input().split()))
for j in arr:
    no = False
    if j==1: continue
    elif j==2:
        count += 1
        continue
    for k in range(2, j):
        if j%k==0: #나머지가 없다면 소수가 아니다.
            no = True #소수가 아니라는 증거
            break
    if no==False:
        count += 1
print(count)