N = int(input())
count = 0
i = 0
n = N
break_point=False

if n%5%3==0:
    count += n//5
    n -= n//5*5
    '''TEST
    print("5 count : %d"%count)
    print("5 n : %d"%n)
    '''
    count += n//3
    n -= n//3*3
    '''TEST
    print("3 count : %d"%count)
    print("3 n : %d"%n)
    print()
    '''
else:
    #print("test") #test
    n = N
    while (N-i*5)//5!=0: #5로 나누어지지 않는 만큼
        n = N
        count = 0
        count += n//5-i
        #5로 나누어지는 수를 i를 통해 줄여나간다.
        n -= (n//5-i)*5
        '''TEST
        print("5 count : %d"%count)
        print("5 n : %d"%n)
        '''
        #n 최신화
        count += n//3
        n -= n//3*3
        '''TEST
        print("3 count : %d"%count)
        print("3 n : %d"%n)
        print()
        '''
        #남은 수를 3으로 나눈다.
        i += 1
        if n==0:
            break_point=True
            break
    if N%3==0 and break_point==False:
        n = N
        count = 0
        count += n//3
        n -= n//3*3
    elif n<3 and break_point==False:
        count = -1
if count==0:
    print("-1")
else:
    print(count)
