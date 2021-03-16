#Daily Algorithm Coding
#2021. 03. 16.
#Count Sort, Insert Sort, Selection Sort, Quick Sort
#계수 정렬, 삽입 정렬, 선택 정렬, 빠른 정렬

print("Daily Algorithm Coding")
print("2021. 03. 16.")
print("\nSelection, Insert, Quick, Count\nSort Algorithm\n")

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def ResetArray(arr):
    return [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

#Selection Sort
#가장 작은 값은 '선택'하여 앞으로 옮기는 과정을 반복하여 정렬하는 알고리즘
print("Selection Sort")
arr = ResetArray(arr)
print(arr)
for i in range(len(arr)):
    min = i
    for j in range(i, len(arr)):
        if arr[min]>arr[j]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]
print(arr)
print()

#Insert Sort
#자신보다 작은 값의 뒤에 '삽입'하는 과정을 반복하여 정렬하는 알고리즘
print("Insert Sort")
arr = ResetArray(arr)
print(arr)
for i in range(1, len(arr)):
    #0 ~ len(arr)-1
    for j in range(i, 0, -1):
        #i ~ 0
        if arr[j-1]>arr[j]:
            #앞의 숫자보다 작으면 교체
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: break
print(arr)
print()

#Quick Sort
#피벗을 지정하여 좌우로 나누는 과정을 반복하여 정렬하는 알고리즘
print("Quick Sort")
arr = ResetArray(arr)
print(arr)
def QS(qa, start, end):
    #qa : Quick sort Array
    if start >= end: return
        #이것을 증명한 과정이 있는데 조금 복잡하니
        #if start >= end : return 이것은 그냥 외워서 쓰는 것이 편할 것이다.
        #쓰이는 경우
        #입력받은 범위 내에서 오른쪽에서부터 피벗보다 작은 값을 찾는데 없어서
        # 그대로 재귀 함수를 호출한 경우
        #입력받은 범위 내의 값이 두 개일 때 정렬 후 재귀 함수를 호출한 경우
        #입력받은 범위 내의 값이 한 개일 경우
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and arr[left]<=arr[pivot]:
            left += 1
        while right > start and arr[right]>=arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    QS(arr, start, right-1)
    QS(arr, right+1, end)
QS(arr, 0, len(arr)-1)
#index 값으로 사용할 예정이기  때문에 len(arr)에서 -1을 해주었다.
print(arr)
print()

#Count Sort
#정렬할 숫자들에서 각 숫자가 몇개씩 사용되었는지 세서
# 숫자 순서대로 사용되었던 만큼 출력하여 정렬하는 알고리즘
print("Count Sort")
arr = ResetArray(arr)
CSResult = []
print(arr)
CSArr = [0 for i in range(max(arr)+1)]
#0도 포함하고 있기 때문에 max(arr)에 +1을 해주었다.
#CSArr : Count Sort Array
for i in arr:
    CSArr[i] += 1
for i in range(len(CSArr)):
    for j in range(CSArr[i]):
        CSResult.append(i)
print(CSResult)
print("\nThank You :)")