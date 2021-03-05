'''
115 Page
왕실의 나이트
'''

'''

8 x 8 좌표 평면
특정한 한 칸에 나이트가 서 있다.

나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력

행 1~8
열 a~h

index 0 : 행 가로로 이어지는
index 1 : 열 세로로 이어지는

'''

knight = list(map(int, input().split()))
step = [(1,2),(-1,2),(2,1),(2,-1),(-2,-1),(-2,1),(1,-2),(-1,-2)]
move = [0, 0]
count = 0

for i in step:
    move = knight[:]
    #move = knight 라고 대입하게 되면 복사가 아닌 move 변수가 knight 리스트를 참조하게 되어서
    # move변수가 수정되면 knight 리스트도 같게 수정되게 된다.
    # 그래서 참조가 아닌 복사가 되도록 knight[:] 라고 사용하였다.
    #print() #test
    #print(move) #test
    move[0] += i[0]
    move[1] += i[1]
    #print(move) #test
    if 0<move[0]<9 and 0<move[1]<9:
        count += 1
        #print(count) #test

print(count)