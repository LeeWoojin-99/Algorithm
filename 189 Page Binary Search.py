#189 Page
#Binary Search
#이진 탐색

'''
데이터가 무작위일 때는 사용할 수 없다.
이진 탐색이란 찾으려는 데이터와 중간점 위치에 있는 데이터를
반복적으로 비교하여 우너하는 데이터를 찾는 탐색 과정이다.
'''
'''
첫 번째 줄 입력 : 원소의 개수 n, 찾아야 하는 값 target을 공백으로 구분하여 입력
두 번째 줄 입력 : 정렬된 원소들을 공백으로 구분하여 입력

찾아야 하는 값 target이 몇 번째 원소인지 출력
'''

def BinarySearch(array, target, start, end):
    if start > end:
        return None
    mid = int((start+end)/2)
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BinarySearch(array, target, start, mid-1)
    else:
        return BinarySearch(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = BinarySearch(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


''' 입력 예시
10 7
1 3 5 7 9 11 13 15 17 19
'''