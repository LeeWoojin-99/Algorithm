'''
226 Page
효율적인 화폐 구성
Dynamic Programming Algorithm Problem
'''
''' 문제 설명
N가지 종류의 화폐
화폐들의 개수를 최소한으로 이용하여 그 가치의 합이 M원
'''
''' 입력 및 출력 조건
입력 조건
첫째 줄 : N, M이 공백으로 구분되어 입력
2~N번째 줄 : 각 화폐의 가치가 공백으로 구분되어 입력
출력 조건
첫째 줄에 경우의 수 X를 출력
'''

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)

d = [99999]*(m+1)
#화폐의 개수를 담는 d
#인덱스 값이 금액이며 그 금액의 화폐 개수가 그 인덱스 값의 요소
d[0] = 0 #0원은 화폐 0개이므로 0으로 초기화, 추후에 
for i in range(n): #주어진 화폐 단위를 바꾸어가는 반복문
    for j in range(arr[i], m+1): #금액을 작은 값에서 큰 값으로 늘려가는 반복문
        if d[j-arr[i]] != 99999:
            #d[ j - arr[i] ] : 현재 금액에서 현재 단위를 뺀 값
            d[j] = min(d[j], d[j-arr[i]]+1)
            #+1 : 현재 단위를 뺐으니 화폐 개수에 현재 단위의 화폐의 개수 한 개를 덧셈

if d[m] == 99999:
    print(-1)
else:
    print(d[m])

for i in range(len(d)):
    print("{} : {}".format(i, d[i]))

'''
2 15
2
3
'''
'''
3 4
3
5
7
'''