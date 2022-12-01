# mobitel

import heapq
def solution(words):
    def heap(iter):
        h, result,result1 = [], [], []
        for i in iter:
            heapq.heappush(h, i)
        for i in range(len(h)):
            result.append(int(iter.index(heapq.heappop(h)) + 1))
            # result1.append(heapq.heappop(h))
        
        print(result)
        print(result1)
        return result[:2]

    # words = list(str(input()))

    split_point = heap(words[1:])

    tmp = sorted(split_point)
    print(tmp)
    result = []
    result.append(words[0:tmp[0]])
    result.append(words[tmp[0]:tmp[1]])
    result.append(words[tmp[1]:])
    print(result)

solution(['m','o','b','i','t','e','l'])
# solution(['a','r','r','e','s','t','e','d'])