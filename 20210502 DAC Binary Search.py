'''
2021. 05. 03.
Daily Algorithm Coding
Binary Search
'''

arr = [1,2,3,4,5,7,8]

def bs(start, end, target, arr):
	if start > end: return None

	mid = (start+end)//2

	if arr[mid] == target:
		return mid
	if arr[mid] < target:
		return bs(mid+1, end, target, arr)
	if arr[mid] > target:
		return bs(start, mid-1, target, arr)

print(bs(0, len(arr)-1, 5, arr))