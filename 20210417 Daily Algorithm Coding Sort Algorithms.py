'''
2021. 04. 17.
Daily Algorithm Coding
Sort Algorithms
1. Select Sort
2. Insert Sort
3. Quick Sort
4. Count Sort
5. Quick Sort with python advantage
'''

def reset_arr():
	global arr
	arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

arr = []
reset_arr()
length = len(arr)


#Select Sort Algorithm Code
print("Select Sort")
print(arr)

for i in range(length):
	min_index = i

	for j in range(i, length):
		if arr[min_index] > arr[j]:
			min_index = j

	arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
print()


#Insert Sort Algorithm Code
print("Insert Sort")
reset_arr()
print(arr)

for i in range(1, length):
	for j in range(i, 0, -1):
		if arr[j] < arr[j-1]:
			arr[j], arr[j-1] = arr[j-1], arr[j]
		else:
			break
			#arr[j] > arr[j-1]
			#이미 앞에는 정렬이 되어있기 때문에
			#break로 불필요한 연산을 하지 않는다.

print(arr)
print()


#Quick Sort Algorithm Code
print("Quick Sort")
reset_arr()
print(arr)

def quick_sort(start, end, arr):
	if start >= end:
		return

	pivot = start
	left = start+1
	right = end

	while left <= right:
		while left <= end and arr[left] <= arr[pivot]:
			left += 1
		while right > start and arr[right] >= arr[pivot]:
			right -= 1

		if left > right:
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:
			arr[left], arr[right] = arr[right], arr[left]

	quick_sort(start, right-1, arr)
	quick_sort(right+1, end, arr)

quick_sort(0, length-1, arr)
print(arr)


#Count Sort Algorithm Code
print("Count Sort")
reset_arr()
print(arr)

count = [0]*(max(arr)+1)

for i in arr:
	count[i] += 1

for i in range(len(count)):
	for j in range(count[i]):
		print(i, end=' ')
print()
print()


#Quick Sort Algorithm Code with Python Advantage
print("Quick Sort Python")
reset_arr()
print(arr)

def quick_sort_python(arr):
	if len(arr) <= 1:
		return arr

	pivot = arr[0]
	tail = arr[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

print(quick_sort_python(arr))
