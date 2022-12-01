n = int(input())

big = []
ranking = [1] * n
for _ in range(n):
    wei, tall = map(int, input().split())
    big.append((wei, tall))

for i in range(len(big)):
    for j in range(i, len(big)):
        if big[i][0] > big[j][0]:
            if big[i][1] > big[j][1]:
                ranking[j] += 1
            else:
                continue
        elif big[i][0] < big[j][0]:
            if big[i][1] < big[j][1]:
                ranking[i] += 1
            else:
                continue
        else:
            continue


print(*ranking)

