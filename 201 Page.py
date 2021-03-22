'''
201 Page
떡볶이 떡 만들기
Binary Search Algorithm Problem

문제 설명
절단기 높이 H
높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
손님이 요청한 총 길이 M
적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성

입력 조건
첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
둘째 줄에 떡의 개별 높이가 주어진다.

입력 예시
4 6
19 15 10 17
'''

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
h = 1

def BS(BSarr, target):
    sum = 0
    for i in range(len(BSarr)):
        BSarr[i] -= target
    for i in range(len(BSarr)):
        if BSarr[i] > 0:
            sum += BSarr[i]
    return sum

total = BS(arr[:], h)

while total >= m:
    h += 1
    total = BS(arr[:], h)

print(h-1)