'''
321 Page
럭키 스트레이트
realization problem
'''

#n = str(input())
n = str(123402)
mid = len(n)//2
left, right = 0, 0

for i in range(mid):
	left += int(n[i])
for i in range(mid,len(n)):
	right += int(n[i])

if left == right:
	print("LUCKY")
else:
	print("READY")