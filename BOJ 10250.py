T = int(input())
total = [0 for i in range(T)]
for i in range(T):
    H, W, N = list(map(int, input().split()))

    Y = N//H if N%H==0 else N//H+1 #호수
    X = H if N%H==0 else N%H #층수
    

    X = str(X)
    Y = '0'+str(Y) if Y<10 else str(Y)

    total[i] = X+Y
for i in total:
    print(i)