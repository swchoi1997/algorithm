a, b = map(int,input().split())

num = [0] * (b + 1)
num[1] = 1
tmp = 2
cnt = 0
for i in range(2, len(num)):
    if tmp == cnt:
        tmp += 1
        cnt = 0
    num[i] = num[i - 1] + tmp
    cnt += 1

print(num[b] - num[a - 1])