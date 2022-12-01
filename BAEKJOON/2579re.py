import sys
sys.setrecursionlimit(10000000)

n = int(input())
stair = []
stair.append(0)
for _ in range(n):
    stair.append(int(input()))

#memorization
stair_max = [0] * (n + 1)

def dp(stair, n):
    if n  == 1:
        return stair[1]
    elif n == 2:
        return stair[1] + stair[2]
    elif n == 0:
        return 0
    else:
        if stair_max[n] != 0:
            return stair_max[n]
        stair_max[n] = max(stair[n] + stair[n - 1] + dp(n - 3), stair[n] + dp(n -2))

print(dp(stair, n))