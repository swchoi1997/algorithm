a = int(input())

b = []
for _ in range(a):
    i, j = map(int, input().split())
    b.append((i,j))

for x in b:
    print(x[0] + x[1])