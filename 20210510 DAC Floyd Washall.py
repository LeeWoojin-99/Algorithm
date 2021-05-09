'''
2021. 05. 10.
Daily Algorithm Coding
Floyd Washall
'''

def distance_check():
	print("\ndistance check function")
	for i in range(1, n+1):
		for j in range(1, n+1):
			print("{:3}".format(distance[i][j]), end=' ')
		print()

INF = 99
n, e = map(int, input().split())
distance = [[INF]*(n+1) for _ in range(n+1)]

distance_check()

for i in range(n+1):
	distance[i][i] = 0

distance_check()

for _ in range(e):
	a, b, dist = map(int, input().split())
	distance[a][b] = dist

distance_check()

for k in range(n+1):
	for i in range(n+1):
		for j in range(n+1):
			distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

distance_check()


''' Floyd Washall Input Data
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
node
edge
edge data
edge data : start node, end node, distance
'''