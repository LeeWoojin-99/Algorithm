#180 Page
#성적이 낮은 순서로 학생 출력하기

''' 문제 설명
첫 번째 줄 입력 : 학생 수 N 입력
두 번째 줄 ~ 입력 : 학생의 이름과 점수를 공백으로 구분되어 입력

성적이 낮은 순서대로 학생의 이름을 출력
'''

n = int(input())
dicStudent = []
for i in range(n):
    x, y = input().split()
    dicStudent.append((int(y), x))
dicStudent = sorted(dicStudent, key=lambda std: std[0])
for i in range(len(dicStudent)):
    print(dicStudent[i][1])

'''
2
홍길동 95
이순신 77
'''