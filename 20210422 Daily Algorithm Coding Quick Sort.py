'''
2021. 04. 22.
Daily Algorithm Coding
Quick Sort
'''

arr = [4,6,7,4,1,9,8,4,3,5]

def qs(start, end, arr):
	if start >= end: return

	pivot = start
	left = start+1
	right = end

	while left <= right:
		while left <= end and arr[left] <= arr[pivot]: left += 1
		while right > start and arr[right] >= arr[pivot]: right -= 1

		if left > right:
			arr[pivot], arr[right] = arr[right], arr[pivot]
		else:
			arr[left], arr[right] = arr[right], arr[left]

	qs(start, right-1, arr)
	qs(right+1, end, arr)

print(arr)
qs(0, len(arr)-1, arr)
print(arr)