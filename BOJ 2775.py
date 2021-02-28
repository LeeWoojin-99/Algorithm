def func(k, n):
    total=0 #호수의 인구 수가 담길 변수 total
    if n==1: #호수가 1이라면
        return 1 #그 호수의 인구로 1을 반환
    elif k==1: #층수가 1이라면
        for i in range(1, n+1): #호수만큼 반복
            total+=i #total에 1부터 호수까지 더한 값
    else: #층수가 1이 아니라면
        for i in range(1, n+1): #호수만큼 반복
            total+=func(k-1, i)
            #현재 층의 호수의 인구를 구하기 위한 과정
    return total #현재 층의 호수를 반환

T = int(input())
result = [0 for i in range(T)]

for i in range(T):
    k = int(input())
    n = int(input())
    result[i] = func(k, n)

for i in result:
    print(i)

'''
def cal_people(f, w, floor_0):
    floor_list = []
    sum = 0
    if w == 1:
        return 1
    if f == 0:
        return floor_0[w - 1]
    for j in range(w):
        sum += floor_0[j]
        floor_list.append(sum)
    return cal_people(f - 1, w, floor_list)
 
T = int(input())
floor_0 = list(range(1, 15))
for i in range(T):
    k = int(input())
    n = int(input())
    people = cal_people(k, n, floor_0)
    print(people)
'''