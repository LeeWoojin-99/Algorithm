'''
BOJ 1929
소수 구하기
'''

M, N = map(int, input().split())
check = [0] * (N + 1) # 소수 확인을 위한 용도

for i in range(2, N + 1) : # 에라토스테네스의 체 이용
    if check[i] == 0 :
        if i >= M :
            print(i)
        for j in range(i*2, N + 1, i) :
            if check[j] == 0 :
                check[j] = 1