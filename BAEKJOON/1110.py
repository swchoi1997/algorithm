a = int(input())
inia = a
cnt = 0
while True:
    na = (a % 10) * 10+ (((a // 10) + (a % 10)) % 10)
    cnt += 1
    if na == inia:
        print(cnt)
        break
    a = na

