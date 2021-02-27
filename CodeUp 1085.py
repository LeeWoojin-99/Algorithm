data=input().split(' ') #공백으로 구분하여 숫자들을 입력받는다.
data=list(map(int,data)) #숫자 연산을 할 예정이기 때문에 입력받은 값을 정수형으로 변환한다.

#변수 h, b, c, s는 Hz, bit, channel, time이다.
h=data[0]
b=data[1]
c=data[2]
s=data[3]
total=h*b*c*s #간소화하지 않은 데이터의 저장 용량의 값
data_unit={1:'bit',2:'byte',3:'KB',4:'MB',5:'GB',6:'TB'} #데이터 단위로 사용하기 위한 딕셔너리 자료형
i=1 #데이터 단위에 쓰이기 위한 변수

def func(data1024):
    global i
    global data_unit
    if data1024<8 and i==1: #저장 용량의 크기가 8bit보다 작아서 단위가 변하지 않아도 되는 경우
        print(data1024, end=data_unit[i]+'\n') #출력
    elif data1024>8 and i==1: #저장 용량의 단위가 bit에서 byte로 넘어가야 하는 경우
        i=i+1 #다음 단위로 넘어간다.
        func(data1024/8) #1byte는 8bit이기때문에 8로 나눈 값으로 func 함수를 재호출한다.
    elif data1024>1024: #저장 용량의 단위가 byte 이상의 단위에서 그 다음 단위로 넘어가야 하는 경우
        i=i+1
        func(data1024/1024) #bit를 제외하고 다음 단위로 넘어가기 위해서 1024로 나눈 값으로 func 함수를 재호출한다.
    else: #저장 용량의 단위를 바꿀 필요가 없는 경우
        if data1024/1024>=0.1 and i<4:
            data1024=data1024/1024
            i=i+1
            print("%.1f"%data1024, end=' '+data_unit[i]+'\n') #출력
        else:
            print("%.1f"%data1024, end=' '+data_unit[i]+'\n') #출력

if h<=48000 and b<=32 and b%8==0 and c<=5 and 1<=s<=6000: #입력 조건
    func(total)
else:
    print("입력값이 잘못되었습니다.")