'''
V : 높이
A : 낮에 올라가는 높이
B : 밤에 미끄러지는 높이
day : 진행 날짜

1. 낮에 올라가기
2. 날짜가 지나가기
3. 밤에 내려가기
1 2 3 반복
'''
A, B, V = list(map(int, input().split()))
day=(V-A)/(A-B)

print(int(day+1 if (day+1)%1==0 else day+2))

