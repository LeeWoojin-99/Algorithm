'''
2021. 05. 14.
Daily Algorithm Coding
Quick Sort
'''

arr = [6,2,1,4,3,5]

def QS(start, end, arr):
    if start >= end: return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] < arr[pivot]: left += 1
        while right > start and arr[right] > arr[pivot]: right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    QS(start, right-1, arr)
    QS(right+1, end, arr)

print(arr)
QS(0, len(arr)-1, arr)
print(arr)
