'''
313 Page
문자열 뒤집기
Greedy Algorithm Problem
'''
'''
 문제 설명
0과 1로만 이루어진 문자열 S
S에 있는 모든 숫자를 전부 같게 만들려 한다.
S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것.
뒤집기의 최소 횟수를 구하시오.

 입력 조건
첫째 줄 : 0과 1로만 이루어진 문자열 S

 출력 조건
첫째 줄 : 다솜이가 해야 하는 행동의 최소 횟수를 출력
'''
''' 문제 풀이
문자열에서 0으로 시작하는 것과 1로 시작하는 것 둘 중에서
어느 것이 더 많은지 
'''

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) -1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

''' 입력 예시
0001100
'''