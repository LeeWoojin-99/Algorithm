'''
322 Page
문자열 재정렬
realization problem
'''

data = 'AJKDLSI412K4JSJ9D'

str_data = []
int_data = 0

for i in data:
	if ord(i) < 58:
		int_data += int(i)
	else:
		str_data.append(i)

for i in range(len(str_data)-1):
	for j in range(i, -1, -1):
		if str_data[j+1] < str_data[j]:
			str_data[j+1], str_data[j] = str_data[j], str_data[j+1]
		else:
			break

result = str_data
result.extend(str(int_data))

for i in result: print(i, end='')

'''
K1KA5CB7
AJKDLSI412K4JSJ9D
'''