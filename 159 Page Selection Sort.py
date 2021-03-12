#159 Page Selection Sort
Arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(len(Arr)):
    MinIndex = i
    for j in range(i+1, len(Arr)):
        if Arr[MinIndex]>Arr[j]:
            MinIndex = j
    Arr[i], Arr[MinIndex] = Arr[MinIndex], Arr[i]
print(Arr)
