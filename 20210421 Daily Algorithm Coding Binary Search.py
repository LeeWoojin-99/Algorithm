'''
2021. 04. 21.
Daily Algorithm Coding
Binary Search
'''

def binary_search(start, end, arr, target):
	if start > end: return None

	mid = (start+end)//2
	
	if arr[mid] == target:
		return mid
	elif arr[mid] < target:
		return binary_search(mid+1, end, arr, target)
	elif arr[mid] > target:
		return binary_search(start, mid-1, arr, target)


n, target = map(int, input().split())

arr = list(map(int, input().split()))

print(binary_search(0, len(arr), arr, target))

''' 입력 예시
10 7
1 3 5 7 9 11 13 15 17 19
'''