n, k = map(int,input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))


result = 0
for i in range(n - 1, -1, -1):
    if coins[i] > k:
        continue

    cnt = k // coins[i]
    k = k - (cnt * coins[i])

    result += cnt

print(result)