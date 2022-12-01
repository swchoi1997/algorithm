n, m = map(int,input().split())

line = []
line6 = []
for i in range(m):
    a, b = map(int,input().split())
    line.append(b)
    line6.append(a)
    
line.sort()
line6.sort()

if n <= 6:
    print(min(line6[0], line[0] * n))
    exit()
money = 0
for i in range(n // 6):
    money += min(line6[0], line[0] * 6)
money += min(line6[0], (line[0] * (n % 6)))

print(money)
