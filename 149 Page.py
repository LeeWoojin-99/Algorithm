#149 Page 음료수 얼려 먹기
''' 문제 설명
N x M 크기의 얼음 틀
0 : 구멍이 뚫려 있는 부분
1 : 칸막이가 존재하는 부분

입력
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.

출력
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
'''
''' 문제 풀이를 위한 메모
모든 얼음 틀의 0은 '탐색되지 않은 상태'로 시작한다.
HoleCheck 변수에 정보가 없다면 '탐색되지 않은 상태'이다.
얼음 틀을 탐색하여 '탐색되지 않은 상태'인 0을 찾는다. 1번.
0이 탐색되면 해당 0과 이어진 0을 모두 찾는다. 2번.
0이 이어져있는지 어떻게 확인할 것인가 ?
찾아진 0은 '탐색된 상태'가 된다. 3번.
1, 2, 3번을 반복하며 1번이 이루어진 횟수가 총 아이스크림의 개수이다.
'''

def DFS(x, y):
    #Depth First Search
    #print("%d, %d : DFS funciton start"%(x, y)) #test
    if not( 0<=x<M and 0<=y<N ):
        #탐색 범위가 얼음틀의 범위를 벗어난다면
        #print("not ice frame") #test
        return #리턴하여 함수를 벗어남
    if arrIceFrame[y][x]=='0' and HoleCheck.count((x, y))==0:
        #print("ice hole") #test
        HoleCheck.append((x, y))
        #탐색되고 있는 장소가 0이라면
        ''' test code
        print("\nDFS를 호출한 위치 %d, %d"%(x, y))
        DFS(x-1, y)
        print("\nDFS를 호출한 위치 %d, %d"%(x, y))
        DFS(x, y-1)
        print("\nDFS를 호출한 위치 %d, %d"%(x, y))
        DFS(x+1, y)
        print("\nDFS를 호출한 위치 %d, %d"%(x, y))
        DFS(x, y+1)
        '''
        DFS(x-1, y)
        DFS(x, y-1)
        DFS(x+1, y)
        DFS(x, y+1)
        return
        #'탐색된 상태'로 바뀌게 된 0의 정보를 리턴
    '''test code
    elif not arrIceFrame[y][x]=='0':
        print("not ice hole")
    elif not HoleCheck.count((x, y))==0:
        print("ice hole but it is already searched")
    '''
    return #탐색되고 잇는 장소가 0이 아닐경우


N, M = list(map(int, input().split()))
arrIceFrame = [0 for i in range(N)]
HoleCheck = [] #'탐색된 상태'의 0의 정보가 들어오는 변수
nCount = 0
for i in range(N):
    arrIceFrame[i] = input()
#print("\nN, M : {}, {}\narrIceFrame : {}\n".format(N, M, arrIceFrame)) #input test

for j in range(N):
    for i in range(M):
        if arrIceFrame[j][i]=='0' and HoleCheck.count((i, j))==0:
            #'탐색되지 않은 상태'의 0이라면
            #print("\nDFS start") #test
            #print(i, j) #test
            DFS(i, j)
            #DFS 함수의 리턴값은 '탐색된 상태'로 바뀌게 된 0의 정보
            nCount += 1
print(nCount)

'''
입력 예제 1
4 5
00110
00011
11111
00000

입력 예제 2
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000111111
00000001111111
01111111110000
00011111111000
00000001111111
11111111110000
11100011111111
11100011111111
11100011111111
'''