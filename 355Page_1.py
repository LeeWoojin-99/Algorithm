'''
355 Page
인터넷을 참고하여 코딩
'''
from collections import deque

def check_map(map_data):
    print("check_map function")
    for y in range(len(map_data)):
        for x in range(len(map_data)):
            print(map_data[y][x], end=' ')
        print()
    print()

def can_move(cur1, cur2, new_board):
    Y, X = 0, 1 # 
    cand = [] # 이동할 수 있는 경우가 담긴 리스트
    DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)] # 이동에 쓰이는 데이터

    for dy, dx in DELTAS:
        # nxt : 이동했을 때의 좌표
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)

        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            # 이동한 좌표가 안전한지 확인
            cand.append((nxt1, nxt2)) # 안전하다면 cand에 추가

    # 회전
    if cur1[Y] == cur2[Y]: # 가로 방향 일 때
        # y좌표가 같다면 가로 방향이다.
        UP, DOWN = -1, 1 # 회전할 때 사용되는 데이터. 위로 회전, 아래로 회전
        for d in [UP, DOWN]:
            # 회전
            if new_board[cur1[Y]+d][cur1[X]] == 0 and new_board[cur2[Y]+d][cur2[X]] == 0:
                # 회전했을 때의 좌표가 안전한지 확인
                cand.append((cur1, (cur1[Y]+d, cur1[X]))) # cur1을 중심으로 회전
                cand.append((cur2, (cur2[Y]+d, cur2[X]))) # cur2를 중심으로 회전
    else: # 세로 방향 일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X]+d] == 0 and new_board[cur2[Y]][cur2[X]+d] == 0:
                cand.append(((cur1[Y], cur1[X]+d), cur1))
                cand.append(((cur2[Y], cur2[X]+d), cur2))

    return cand

def solution(board):
    # board 외벽 둘러싸기
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]
    check_map(new_board)
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]
    check_map(new_board)

    # 현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])
    print(confirm)

    while que:
        cur1, cur2, count = que.popleft()
        # cur1, 2 : 로봇의 위치
        # count : 시간

        if cur1 == (N, N) or cur2 == (N, N): return count
        # 로봇이 N, N에 도착했다면 count를 리턴

        for nxt in can_move(cur1, cur2, new_board):
            # 이동할 수 있는 로봇의 위치들이 담긴 리스트 자료형을 리턴한 can_move 함수
            # nxt : 이동할 수 있는 위치
            
            # 이동할 수 있는 위치들을 모두 알아낸 후에 그 위치가 중복된 위치인지 확인해가며
            # 중복된 위치가 아니라면 이동

            if nxt not in confirm:
                # 이동했던 위치는 confirm에 담기는데
                # 이동할 수 있는 위치가 이동했던 위치인지 확인
                que.append((*nxt, count+1))
                # 언패킹을 통하여 3개의 데이터를 que에 append
                # 다음에 이동할 데이터
                confirm.add(nxt)
                # 이동할 예정이니 다음에 중복되지 않도록 confirm에 츄가
                # dictionary 자료형이라 append가 아닌 add 메서드를 사용

#print(solution([[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]))
print(solution([[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]))