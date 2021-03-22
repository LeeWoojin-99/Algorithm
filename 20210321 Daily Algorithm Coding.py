#2021. 03. 21.
#Daily Algorithm Coding

#Binary Search
#이진 탐색
print("Binary Search")
def BS(arr, target, start, end):
    if start > end:
        return None
    mid = int((start+end)/2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return BS(arr, target, start, mid-1)
    elif arr[mid] < target:
        return BS(arr, target, mid+1, end)
'''
n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
'''
n, target = 10, 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
result = BS(arr, target, 0, n-1)
print("n : {0}\ntarget : {1}\narr : {2}".format(n, target, arr))
if result == None:
    print("None")
else:
    print(result+1)

''' 입력 예시
10 7
1 3 5 7 9 11 13 15 17 19
'''

