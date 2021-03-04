'''
96 Page
숫자 카드 게임
'''

N, M = list(map(int, input().split()))
result = []
for i in range(N):
    arr = list(map(int, input().split()))
    result.append(min(arr))
print(max(result))