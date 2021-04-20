import heapq

def solution(food_times, k):
    # k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
    
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식의 시간
    length = len(food_times) # 남아있는 음식의 개수

    # (sum_valse + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수)와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # 다음 음식을 모두 먹어도 시간을 초과하지 않는지 확인하는 조건문
        # 조건문을 통과했다면 해당 음식을 먹어서 없애는 동작을 수행
        now = heapq.heappop(q)[0] # 먹어서 없앨 음식
        sum_value += (now - previous) * length # 음식을 먹었으니 먹는데 걸린 시간만큼 처리
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    result = sorted(q, key = lambda x: x[1])
    # 인덱스 1의 값은 음식의 번호이다.
    # 남아있는 음식들을 음식의 번호대로 정렬한다.
    return result[(k - sum_value) % length][1]
    # k - sum_value : 음식들이 없어지고 남아있는 시간
    # length : 남아있는 음식들의 개수

print(solution([3,1,2],5))
#print(solution([4,2,9,2,8], 17))
#print(solution([946,314,757,322,559,648,932,234,543],3021))

'''
시간이 작은 음식을 없애가며 진행해간다.

음식을 없애기 전에 없애는 데에 시간이 얼마나 소요되고
그 시간이 제한 시간 k를 넘기는지 비교한다.

넘기지 않는다면 음식을 없애고

넘긴다면 음식을 없애는 과정을 멈추고
없어지지 않고 남아있는 음식중에서
제한시간에서 소요된 시간을 제외하여 남아있는 시간을 구한다.
남아있는 시간이 지나면 어떤 음식이 나올지 구한다.
남아있는 시간이 지나는 동안은 음식이 없어지지 않으므로 쉽게 구할 수 있다.
'''