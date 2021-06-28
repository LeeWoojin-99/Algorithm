'''
BOJ 2751
수 정렬하기 2
Quick Sort를 이용한다면 최악의 경우 O(N^2)의 시간복잡도를소모하기 때문에
재귀의 깊이가 파이썬의 기본 재귀 깊이 제한인 1000을 넘어가며나서 시간 초과 이전에 먼저 런타임 에러를 받고
강제 종료된다.
'''

import sys

def QS(start, end, arr):
    if start >= end: return

    pivot = start
    left = start +1
    right = end

    while left <= right:
        while left <= end and arr[left] < arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    QS(start, right-1, arr)
    QS(right+1, end, arr)

n = int(input())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

QS(0, len(arr)-1, arr)

for i in arr:
    print(i)