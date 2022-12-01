import sys
input = sys.stdin.readline

a,b = map(int, input().split())

maps = []
for _ in range(a):
    bnw = input()
    maps.append(list(bnw))

result = 64
for i in range(a + 8 - 1):
    for j in range(b + 8 - 1):
        count_w = 0
        count_b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if maps[x][y] != 'W': # W로 시작하는 경우
                        count_w += 1
                    elif maps[x][y] != 'B': # B 로 시작하는경우 1, 3, 5, 7 번쨰가  B 가 아니면
                        count_b += 1
                elif (x + y) % 2 == 1:
                    if maps[x][y] != 'W': # B 로 시작하는 경우 2,4,6,8 번째가 W 아닌경우
                        count_b += 1
                    elif maps[x][y] != 'B':
                        count_w += 1
        reuslt = min(result, count_b, count_w)
print(result)
        