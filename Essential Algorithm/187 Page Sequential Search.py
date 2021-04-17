#187 Page
#Sequential Search
#순차 탐색

def SequentialSearch(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
n, target = input().split()
n = int(n)
array = input().split()

print(SequentialSearch(n, target, array))