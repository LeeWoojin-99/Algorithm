'''
2021. 06. 03.
Daily Algorithm Coding
Binary Search Algorithm
이진 탐색 알고리즘
'''

arr = [1,2,3,4,5,6,7,8,9]

def BS(start, end, arr, target):
    pivot = (end+start)//2
    
    if arr[pivot] == target:
        return pivot
    elif arr[pivot] < target:
        return BS(pivot+1, end, arr, target)
    else:
        return BS(start, pivot-1, arr, target)

print(BS(0, len(arr)-1, arr, 4))