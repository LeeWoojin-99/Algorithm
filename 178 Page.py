#178 Page
#위에서 아래로

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr, reverse=True)
for i in arr:
    print(i, end=' ')
print()

''' 입력 예시
3
15
27
12
'''