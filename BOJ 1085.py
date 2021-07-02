'''
BOJ 1085
직사각형에서 탈출
'''

x, y, w, h = map(int, input().split())

arr = [0 for _ in range(4)]

arr[0] = h-y # 위쪽
arr[1] = w-x # 오른쪽
arr[2] = y # 아래쪽
arr[3] = x # 왼쪽

print(min(arr))