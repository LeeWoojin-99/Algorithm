'''
197 Page
부품 찾기
Binary Search Algorithm Problem
이진 탐색 알고리즘 문제
'''
''' 문제 설명
가게 안에 부품 N개 보유
각 부품은 정수 형태의 고유한 번호가 존재
손님이 M개 부품을 구매
가게 안에 손님이 구매할 부품이 모두 있는지 확인하는 프로그램 작성
'''
''' 입출력 조건
입력 조건
첫째 줄에 정수 N
둘째 줄에 공백으로 구분하여 N개의 정수
셋째 줄에 정수 M
넷째 줄에 공백으로 구분하여 M개의 정수

출력 조건
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes, 없으면 no를 출력
'''
''' 입력 예시
5
8 3 7 9 2
3
5 7 9
'''
n = int(input())
nArr = list(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))
print(n, nArr)
print(m, mArr)

def BS(arr, target, start, end):
    #BS : Binary Search
    if start > end:
        return 'No'
    mid = int((start+end)/2)
    if arr[mid] == target:
        return 'Yes'
    elif arr[mid] > target:
        return BS(arr, target, start, mid-1)
    elif arr[mid] < target:
        return BS(arr, target, mid+1, end)

for i in mArr:
    print(BS(nArr, i, 0, len(nArr)-1), end=' ')
print()