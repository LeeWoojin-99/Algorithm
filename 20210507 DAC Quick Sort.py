'''
2021. 05. 08.
Daily Algorithm Coding
Quick Sort
빠른 정렬
'''

def qs(start, end, arr):
	if start >= end: return

	pivot = start
	left = start + 1
	right = end

	while left <= right:
		while left <= end and arr[left] < arr[pivot]: left += 1
		while right > start and arr[right] > arr[pivot]: right -= 1

		if left > right:
			arr[right], arr[pivot] = arr[pivot], arr[right]
		else:
			arr[left], arr[right] = arr[right], arr[left]

	qs(start, right-1, arr)
	qs(right+1, end, arr)


arr = [6,2,4,1,3,5]

print(arr)
qs(0, len(arr)-1, arr)
print(arr)