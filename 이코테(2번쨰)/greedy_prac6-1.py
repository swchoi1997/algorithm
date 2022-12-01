# 무지의 먹방 라이브
from queue import PriorityQueue

def solution(food_times, k):
    if sum(food_times) <= k :
        return -1

    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)): # heapq에 오름차순으로 정렬해서 food값을 넣음
        q.put((food_times[i], i + 1)) # ft[0]값과 1 이렇게 번호도 같이 넣음
    
    sum_now, previous = 0
    length = len(food_times) # 먹기가 다 완료된 번호는 빼야하기때문에 이렇게 지정 후 -1 을 해줌

    while sum_now + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0] # get해서 나오는 것 중에  첫번째 원소를 now에 입력
        sum_now += (now - previous) * length
        length -= 1
        previous = now

    answer1 = k - sum_now + 1 
    length2 = len(q.queue)
    temp = (answer1 - 1) // length2
    result = sorted(q.queue, key = lambda x:x[1])
    answer1 -= temp * length2

    return result[answer1 -1][1]