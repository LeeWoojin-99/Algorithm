'''
2021. 04. 27.
Daily Algorithm Coding
Quick Sort
'''

# quick sort code
arr = [8,4,2,5,9,1,3,7,6]

def qs(start, end, arr):
	if start >= end: return arr

	pivot = start
	left = start+1
	right = end

	while left <= right:
		while left <= end and arr[left] <= arr[pivot]: left += 1
		while right > start and arr[right] >= arr[pivot]: right -= 1

		if left > right:
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:
			arr[right], arr[left] = arr[left], arr[right]

	qs(start, right-1, arr)
	qs(right+1, end, arr)

print("QS")
print(arr)
qs(0, len(arr)-1, arr)
print(arr)

# quick sort code with python advantage
arr = [8,4,2,5,9,1,3,7,6]

def qsp(arr):
	if len(arr) <= 1: return arr

	pivot = arr[0]
	tail = arr[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return qsp(left_side) + [pivot] + qsp(right_side)

print("QSP")
print(arr)
print(qsp(arr))