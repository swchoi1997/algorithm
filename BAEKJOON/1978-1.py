n = int(input())
num = list(map(int, input().split()))

count = 0
check1 = 0
check2 = 0

for i in num:
    if i == 1:
        continue
    if i != 1 and i <= 3:
        count += 1
    elif i > 3:
        for j in range(2 , i//2 + 1):
            if i % j != 0:
                check1 += 1
                check2 += 1
            elif i % j == 0:
                check1 -= 1
                check2 += 1
        if check1 == check2:
            count += 1
        check1, check2 = 0, 0
    
print(count)
