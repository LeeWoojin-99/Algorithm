'''
Dynamic Programming
Top-Down
'''
d = [0]*100
def Pibo(x):
    print("f(%d)"%x, end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = Pibo(x-1) + Pibo(x-2)
    return d[x]
Pibo(6)
print("")
'''
      6 
     5 4
    4 3
   3 2
  2 1

6에서 5와 4를 호출한다. 5가 먼저 호출되었기 때문에
5에서 4, 3 ... 이렇게 1까지 간다. 그렇게 5를 구했다면
6에서 호출했던 4로 간다. 4는 이미 5를 구하는 과정에서 구해져 있다.
'''