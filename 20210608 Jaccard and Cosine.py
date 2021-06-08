import math
# 제곱근을 구하는 루트 연산을 할 때 쓰이는 sqrt 메서드를 사용하기 위해서 math 모듈을 import

def Jaccard(a, b):
	result1, result2 = 0, 0
	# result1 : 분자
	# result2 : 분모

	for i in range(len(a)):
		result1 += a[i]*b[i] # 분자를 구하는 부분

		for j in [a[i], b[i]]: # 분모를 구하는 부분
			if j == 1:
				result2 += 1
				break

	return result1 / result2

def Cosine(a, b):
	result1, result2 = 0, 0
	# result1 : 분자
	# result2 : 분모

	for i in range(len(a)):	result1 += a[i]*b[i] # 분자를 구하는 부분
	
	result2_a, result2_b = [], []
	# Cosine(s1v, s2v)일 때 문제에서 나온 공식의 분모는 ||S1v|| * ||S2v|| 로 계산되는데
	# result2_a가 ||S1v||가 담기는 공간, result2_b가 ||S2v||가 담기는 공간입니다.
	for i in [(a, result2_a), (b, result2_b)]: # a의 데이터로 작업한 값이 result2_a에 들어갑니다.
		for j in i[0]: i[1].append(j**2)
		# 공식에서 루트 내부의 시그널 연산이 될 값들을 i[1]에 차례대로 넣어가는 부분

	result2_a = math.sqrt(sum(result2_a))
	# math.sqrt(x) : x의 제곱근을 구합니다. 즉 x에 대해 루트 연산을 합니다.
	# sum(result2_a) : 시그널 연산
	result2_b = math.sqrt(sum(result2_b))
	result2 = result2_a * result2_b # 공식에서 나와있는 것처럼 곱하기 연산

	return result1 / result2
	

s1 = "I am a boy".lower().split()
s2 = "You are not a girl".lower().split()
s3 = "She is a girl".lower().split()
# lower() : 문자열의 모든 문자를 소문자로 변환
# split(x) : x로 데이터를 나눠서 리스트 자료형으로 변환. x는 공백(' ')이 기본값
# "I am a boy"를 lower()를 통하여 "i am a boy"로 변환하였고
# "i am a boy"를 split()을 통하여 ['i', 'am', 'a', 'boy']로 변환하였다.
s4 = list(set(s1) | set(s2) | set(s3))
# list() : 리스트 자료형으로 변환
# set() : 딕셔너리 자료형으로 변환
# 딕셔너리 자료형끼리 | 연산 : 합집합 연산
# dictionary자료형으로 변환한 후 합집합을 구하고 list자료형으로 변환

s1v, s2v, s3v = [[] for _ in range(3)]

for i in [s1, s2, s3, s4]: i.sort() # 정렬

for s in [(s1, s1v), (s2, s2v), (s3, s3v)]: # s1v, s2v, s3v를 구하는 부분
	for i in s4:
		s[1].append(s[0].count(i))

# 1번 문제의 해답 출력
print("1번 문제")
print("S4  : ", end='')
for i in s4: print("%5s"%i, end='')
for i in [(1, s1v), (2, s2v), (3, s3v)]:
	print("\nS%dv : "%i[0], end='')
	for j in i[1]: print("%5d"%j, end='')
print("\n")

print("2번 문제")
for i in [(1, s1), (2, s2), (3, s3), (4, s4)]:
	print("S%d = "%i[0], end='')
	print(i[1])
for i in [(1, s1v), (2, s2v), (3, s3v)]:
	print("S%dv = "%i[0], end='')
	print(i[1])
print("1. 자카드 유사도")
print("-S1, S2 : %.2f"%Jaccard(s1v, s2v))
print("-S2, S3 : %.2f"%Jaccard(s2v, s3v))
print("-S1, S3 : %.2f"%Jaccard(s1v, s3v))
print("2. 코사인 유사도")
print("-S1, S2 : %.2f"%Cosine(s1v, s2v))
print("-S2, S3 : %.2f"%Cosine(s2v, s3v))
print("-S1, S3 : %.2f"%Cosine(s1v, s3v))