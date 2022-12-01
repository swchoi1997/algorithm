from queue import PriorityQueue

def solution(food_times, k):
    if sum(food_times) <= k :
        return -1

    answer = 0
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i + 1)) #다른 정렬기준으로 우선순위 큐에 넣고 싶기때문에 food time을 정렬기준으로함
    
    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    
    target = k - sum_value + 1
    length = len(q.queue)
    temp = (target -1) // length #몇 번 반복한지 알기위해서 targer에서 1을 빼고 나누기함
    result = sorted(q.queue, key = lambda x: x[1]) # q를 정렬하기때문에
    target -= temp * length # temp가 반복 횟수기때문에 길이만큼 곱해서 나온 값을 target에 빼면 어떠한 값이 나오는데
    
    return result[target -1][1]  # 여기서 1을 뺸 값이 두번 째음식이 나옴 0, 1, 2 이순서로 진행되니까
    # 여기서 뒤에 몇번째 값을 정렬해야하는지 나옴