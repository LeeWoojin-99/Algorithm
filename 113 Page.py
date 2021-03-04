'''
113 Page
시각
'''

'''
정수 N 입력

00시 00분 00초부터 N시 59분 59초까지의
모든 시간 중에서 3이 하나라도 포함되는
모든 경우의 수를 구한다.

시 분 초는 각각 두자리 수로 표현

60초 달성 시 0초으로 초기화 후 1분 추가

시 분 초를 문자열로 변환 후 합쳐서
통합된 문자열에 문자 3이 있는지 검사
검사하여 있으면 카운트
'''

N = int(input())
time = [0 for i in range(3)]
count = 0

while time[0]!=N or time[1]!=59 or time[2]!=59:
    time[2] += 1 #1초 증가
    #print(time) #test
    if time[2]==60:
        time[2] = 0
        time[1] += 1
    if time[1]==60:
        time[1] = 0
        time[0] += 1
    
    three_check = str(time[0]) + str(time[1]) + str(time[2])
    if three_check.find('3')!=-1:
        #print("check") #test
        count += 1
print(count)
