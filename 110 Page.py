'''
110 Page
상하좌우
'''

'''
N x N 크기의 정사각형
가장 왼쪽 위 (1, 1)
가장 오른쪽 아래 (N, N)
Left Right Up Down

첫째 줄 입력 : N
둘째 줄 입력 : A가 이동할 계획서 내용
결과 : 최종적으로 도착할 지점의 좌표를 출력
'''

N = int(input())
A = [1, 1]
T = list(map(str, input().split()))

for i in T:
    if i == 'R' and A[0]<N:
        A[1] += 1
    elif i == 'L' and A[0]>1:
        A[1] -= 1
    elif i == 'U' and A[0]>1:
        A[0] -= 1
    elif i == 'D' and A[0]<N:
        A[0] += 1
print(A[0], A[1])