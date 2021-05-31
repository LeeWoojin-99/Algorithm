'''
2021. 05. 31.
Daily Algorithm Coding
Quick Sort Algorithm
'''

arr = [4,6,2,3,1,5]

def QS(start, end, arr):
    if start >= end: return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] < arr[pivot]: left += 1
        # 작은 값을 만날 때까지 left 증가
        # end를 넘어가면 증가 중지
        while right > start and arr[right] > arr[pivot]: right -= 1
        # 큰 값을 만날 때까지 right 감소
        # start와 같아지면 감소 중지
        # arr[right]에서 start가 0일 때 start 보다 낮아지면 -1이라서
        # arr[-1]은 리스트의 범위를 넘어가기 때문에 오류가 발생한다.

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    QS(start, right-1, arr)
    QS(right+1, end, arr)

print(arr)

QS(0, len(arr)-1, arr)
# 인자값 end의 값으로 인수값 len(arr)-1을 입력한다.
# 인자값 end는 인덱스 값으로써 사용되기 때문이다.

print(arr)