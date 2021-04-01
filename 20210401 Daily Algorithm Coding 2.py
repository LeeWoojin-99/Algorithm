'''
2021. 04. 01.
Daily Algorithm Coding 2
Floyd Washall Algorithm
'''

INF = int(99)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

def GraphCheck():
    print("\nDistance Check")
    for i in range(1, len(graph)):
        for j in range(1, len(graph[i])):
            print("{:3}".format(graph[i][j]), end=' ') 
        print()
    print()

GraphCheck()
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
GraphCheck()

''' Floyd
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''