input1=int(input())
input2=input().split(' ')
#input2=list(map(int,input2))
for i in range(input1):
    input2[i]=int(input2[i])
#for문으로 형변환을 해야 정답이 된다. 왜인지를 잘 모르겠음.

j=23
for i in range(input1):
    if j>input2[i]:
        j=input2[i]

print(j) #가장 작은 값을 출력