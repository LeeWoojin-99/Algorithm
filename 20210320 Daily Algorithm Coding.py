#2021. 03. 20.
#daily algorithm coding

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def BS(array, target, start, end):
    if start > end:
        return None
    mid = int((start+end)/2)
    print(start, mid, end)
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return BS(array, target, start, mid-1)
    else:
        return BS(array, target, mid+1, end)

result = BS(array, target, 0, n-1)
if result == None:
    print("no data")
else:
    print(result+1)

''' 입력 예시 1
10 7
1 3 5 7 9 11 13 15 17 19
'''
''' 입력 예시 2
10 8
1 3 5 7 9 11 13 15 17 19
'''