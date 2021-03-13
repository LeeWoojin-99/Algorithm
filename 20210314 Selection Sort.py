#2021 03 14
#Selection Sort
#선택 정렬
#연습

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(arr)
for i in range(len(arr)):
    min = i
    for j in range(i+1, len(arr)):
        if arr[min]>arr[j]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
print(arr)

''' 중요 포인트
for i in range(len(arr)):
for j in range(i+1, len(arr)):
arr[i], arr[min] = arr[min], arr[i]
'''