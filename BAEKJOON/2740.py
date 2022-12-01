a1, b1 = map(int,input().split())
h1 = [list(map(int,input().split())) for _ in range(a1)]
a2, b2 = map(int,input().split())
h2 = [list(map(int,input().split())) for _ in range(a2)]

result = [[0] * b2 for _ in range(a1)]

for i in range(a1):
    for j in range(b2):
        for k in range(b1):
            result[i][j] += h1[i][k] * h2[k][j]

for i in result:
    print(*i)