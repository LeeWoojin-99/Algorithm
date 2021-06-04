'''
359 Page
국영수
Sort Algorithm Problem
'''

number = int(input())
arr = []

for i in range(number):
	data = input().split()
	data[1:] = map(int, data[1:])
	arr.append(tuple(data))

print(arr)
arr.sort(key = lambda x: [-x[1], x[2], -x[3], x[0]])
print()
for i in arr:
	print(i[0])

'''
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
'''