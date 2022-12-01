import sys
sys.setrecursionlimit(10000000)

n = int(input())
stair = []
stair.append(0)
for _ in range(n):
    stair.append(int(input()))

stair_max = [0] * (n + 1)
if n < 3:
    print(sum(stair))
    exit()
else:            
    stair_max[1] = stair[1]
    stair_max[2] = stair[1] + stair[2]

    for i in range(3, n + 1):
        stair_max[i] = max(stair[i] + stair[i - 1] + stair_max[i - 3], stair[i] + stair_max[i - 2])

    print(stair_max[n])


# bottom - up 방식 으로 문제를 풀었을 때