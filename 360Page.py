'''
360 Page
안테나
Sort Algorithm Problem
'''

n = int(input())
arr = list(map(int, input().split()))

distance = []

for i in arr:
    dist = 0

    for j in arr:
        dist += abs(i-j)

    distance.append((i, dist))

distance.sort(key = lambda x: [x[1], x[0]])

print(distance[0][0])

'''
4
5 1 7 9
'''