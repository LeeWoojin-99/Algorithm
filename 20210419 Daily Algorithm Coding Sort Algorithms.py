'''
2021. 04. 19.
Daily Algorithm Coding
Sort Algorithms
1. quick sort
2. quick sort with python advantage
3. select sort
4. insert sort
'''

def reset_arr():
    global arr
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

arr = []
reset_arr()
length = len(arr)

reset_arr()

def qs(start, end, arr):
    if start >= end: return

    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    qs(start, right-1, arr)
    qs(right+1, end, arr)

print("Quick Sort")
print(arr)
qs(0, len(arr)-1, arr)
print(arr)
print()

print("Quick Sort with python advantage")
reset_arr()
print(arr)
def qsp(arr):
    if len(arr) <= 1: return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return qsp(left_side) + [pivot] + qsp(right_side)
print(qsp(arr))
print()

print("Select Sort")
reset_arr()
print(arr)

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[min_index], arr[i] = arr[i], arr[min_index]

print(arr)
print()

print("Insert Sort")
reset_arr()
print(arr)

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break

print(arr)
print()
