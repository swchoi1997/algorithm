INF = 10e9
n, m = map(int, input().split())

friend = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                friend[i][j] = 0
            friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])


resultlist = []
for i in friend:
    resultlist.append(sum(i))

print(resultlist.index(min(resultlist)) + 1)
