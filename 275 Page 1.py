'''
275 Page
Path Compression
경로 압축 기법
'''

def find_parent(parent, x):
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

''' 기존의 find 함수
def find_parent(parent, x):
	if parent[x] != x:
		return find_parent(parent, parent[x])
	return x
'''