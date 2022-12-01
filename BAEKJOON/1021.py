from collections import deque

n, m = map(int,input().split())
number = deque([(i + 1) for i in range(n)])
picknum = list(map(int,input().split()))

cnt = 0
for i in picknum:
    loc = number.index(i) + 1

    while True:
        half = len(number) // 2
        if loc > half + 1:
            if number[-1] != i:
                tmp = number.pop()
                number.appendleft(tmp)
                cnt += 1
            else:
                number.pop()
                cnt += 1
                break
        else:
            if number[0] != i:
                tmp = number.popleft()
                number.append(tmp)
                cnt += 1
            else:
                number.popleft()
                break

print(cnt)