'''
316 Page
무지의 먹방 라이브
Greedy Algorithm Problem
'''

import heapq

def solution(food_times, k):
	answer = 0
	food_length = len(food_times)
	food_rotation = 0
	time_remainder = k

	queue = []
	for i in range(len(food_times)):
		heapq.heappush(queue, (food_times[i], i))

	while queue:
		food_time, food_number = heapq.heappop(queue)

		if time_remainder - (food_times[food_number] - food_rotation) * food_length < 0:
			break
		else:
			time_remainder -= (food_times[food_number] - food_rotation) * food_length
			food_rotation += food_times[food_number] - food_rotation
			food_times[food_number] = 0
			food_length -= 1

	if food_length != 0:
		time_remainder = time_remainder % food_length + 1
		print("%d초를 남기고 남은 음식 확인"%time_remainder)
		print(food_times)
		print("\n남은 음식 중에서 %d번째 음식이 나올 예정\n"%time_remainder)

		count = 0
		for i in range(len(food_times)):
			if food_times[i] != 0:
				count += 1
				if count == time_remainder:
					answer = i+1
					break

		print("%d초 후에 나올 음식은 %d번 음식입니다."%(k, answer))
	else:
		print("남은 음식이 없습니다.")
		answer = -1

	return answer

#solution([3,1,2],5)
#solution([3,1,2],9)
#solution([8,3,7], 14)
solution([946,314,757,322,559,648,932,234,543],3021)