input1=int(input())
input2=list(map(int, input().split()))

if input1<=100:
    for i in range(2):
        for j in input2:
            print(j)
