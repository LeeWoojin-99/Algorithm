'''
2021. 04. 23.
Daily Algorithm Coding
Binary Search
'''

arr = [2,4,1,5,3]

def bs(start, end, target, arr):
	if start > end: return None

	mid = (start+end)//2

	if arr[mid] == target:
		return mid
	if arr[mid] < target:
		return bs(mid+1, end, target, arr)
	if arr[mid] > target:
		return bs(start, mid-1, target, arr)

print(bs(0, len(arr)-1, 6, arr))