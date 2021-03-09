import collections

queue = collections.deque([1,2,3])
#double-ended queue
#양방향에서 데이터를 처리할 수 있다.
#python에서 collections.deque는 list와 비슷하다.

queue.appendleft(4)
#appendleft처럼 append, pop, extend를
# 왼쪽으로부터 추가될 수 있도록 하게한다.
print(queue)

queue.rotate(2)
#rotate 메소드의 인수값만큼 리스트를 회전시켜준다.
print(queue)