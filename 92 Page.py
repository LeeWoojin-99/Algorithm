'''
92 Page

인덱스 값이 다르다면 다른 수로 취급된다.
연속하여 더하다가 다른 수를 더하면 연속하는 횟수가 초기화된다.

N : 배열의 크기
M : 숫자가 더해지는 횟수
K : 연속 가능한 횟수
arr : 배열
'''

'''
더할때마다 변수를 카운트하여 변수가 M과 같은지 확인해야 한다.

내림차순 정렬을 한 배열의 첫 번째 요소를 K만큼 더한 후에 두 번째 요소를 더한다.
이 동작을 반복하며 더한 횟수가 M과 같은지 확인한다.
'''

N, M, K = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = 0
count = 0

arr.sort() #오름차순
arr.reverse() #오름차순을 뒤집어 내림차순

if arr[0]==arr[1]:
    result = arr[0]*M
else:
    while M!=count:
        for i in range(K):
            if M==count:
                break
            result += arr[0]
            count += 1
        if M==count:
            break
        result += arr[1]
        count += 1
print(result)

'''
더하는 것을 모두 수행하지 않고, 수학식으로 해결할 수도 있다.
M/(K+1) : 첫 번째 큰 수가 K번 더해지고 두 번째 큰 수가 1번 더해지는 것을 한 세트로 하였을 때, 세트가 행해지는 횟수
M%(K+1) : 세트가 행해지고 첫 번째 큰 수가 더해지는 횟수
세트가 행해지는 횟수는 두 번째 큰 수가 더해지는 횟수와도 같다.
result = arr[0]*M/(K+1) + arr[0]*M%(K+1) + arr[1]*M/(K+1)
위의 반복문으로 구한 result 값과 같은 값을 더 적은 시간 복잡도로 얻을 수 있다.
'''