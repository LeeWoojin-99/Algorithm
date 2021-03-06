'''
BOJ 1101
Fly me to the Alpha Centauri
'''

'''
우주선 Alpha Centauri

이전 작동시기에 k광년을 이동하였을 때에는
k-1, k 혹은 k+1 광년만을 다시 이동할 수 있다.

처음 작동시킬 경우 -1, 0, 1 광년 이동 가능
1광년 이동 후에는 0, 1, 2광년 이동 가능

x지점에서 y지점을 향해 최소한의 작동 횟수를 구하라.
y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년.

k+1가 y까지의 거리와 같거나 작다면 y-1까지 이동

입력의 첫번째 줄 : 테스트케이스의 개수 T
입력의 두번째 줄 : 현재 위치 x, 목표 위치 y
x는 항상 y보다 작은 값을 가진다.
'''

'''
0 3
1(1) - 1(2) - 1(3)

1 5
1(2) - 2(4) - 1(5)

45 50
1(46) - 2(48) - 1(49) - 1(50)

0 1
1
0 2
1 1
0 3
1 1 1

0 4
1 2 1
0 5
1 2 1 1
0 6
1 2 2 1
0 7
1 2 2 1 1
0 8
1 2 2 2 1

0 9
1 2 3 2 1

'''
'''
제곱수마다 새로운 숫자가 나타난다.

개수
제곱수 : (루트 제곱수)*2 -1
제곱수+1 ~ 제곱수+(루트 제곱수) : (루트 제곱수)*2
제곱수+(루트 제곱수)+1 ~ 다음 제곱수 -1 : (루트 제곱수)*2 +1
'''

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    c = b - a
    num = 1
    while True:
        if num ** 2 <= c < (num + 1) ** 2:
            break
        num += 1
    if num ** 2 == c:
        print((num * 2) - 1)
    elif num ** 2 < c <= num ** 2 + num:
        print(num * 2)
    else:
        print((num * 2) + 1)