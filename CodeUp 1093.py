inp1=int(input()) #첫 번째 줄의 입력을 받는 변수
inp2=input().split(' ') #두 번째 줄의 입력을 받는 변수
#inp2=list(map(int,inp2)) #연산을 하기 위해서 inp2을 정수형으로 형변환
for i in range(inp1):
    inp2[i]=int(inp2[i])
#map을 사용하여 형변환을 하면 오답, for문을 사용하여 형변환을 하면 정답으로 된다. 왜인지는 잘 모르겠다.
stu=[0 for x in range(0,23)] #번호가 불린 횟수를 카운트하기 위한 리스트
     
for i in range(0,inp1):
    #두 번째 줄로 입력받은 데이터를 기반으로
    #번호가 불린 횟수를 카운트하기 위한 반복문
    stu[inp2[i]-1]=stu[inp2[i]-1]+1
    #출석이 불린 학생의 출석 번호가 몇번인지 찾아서 불린 횟수를 카운트하는 과정

for i in range(1,24):
    print(stu[i-1], end=' ')
    #1번부터 번호가 불린 횐수를 순서대로 공백으로 구분하여 한 줄로 출력