N=int(input()) #입력
count=0
n=0 #각 자리의 숫자를 더한 숫자가 담기는 변수 n
N_list=[] #자리마다 수를 분리하여 담는 리스트

while not 0<=N<=99:
    #입력 조건을 충족하는지에 대한 검사
    print("입력이 잘못되었습니다. 다시 입력해주세요.")
    N=int(input())
    
finish=N #맨 처음 지정된 숫자
#print() #test
while finish!=N or count==0: #새로운 수가 처음 입력한 수와 같아질 때까지 무한 루프
    #각 자리수를 분리하여 N_list 리스트에 담는 과정
    N_list=[] #밑의 append를 위해서 N_list를 빈 리스트로 초기화
    N_list.append(N//10)
    N_list.append(N-N_list[0]*10)
    #print(N_list) #test
    n=0 #밑의 for문을 위해서 n을 0으로 초기화
    for i in N_list: n=n+i #분리한 각 자리의 숫자를 더한 n
    #print("분리한 각 자리의 숫자를 더한 값은 %d"%n) #test
    N=N_list[1]*10
    #십의 자리의 수는 기존의 수의 일의 자리의 수,
    N=N+n-n//10*10
    #1의 자리의 수는 새로운 수 n의 일의 자리의 수
    count=count+1
    #print("새로운 수는 %d"%N) #test
    #print() #test
print(count)