n = int(input())

for i in range(n + 1):
    result1 = i
    
    num = list(str(i))
    for j in num:
        result1 += int(j)

    if result1 == n:
        print(i)
        break

    if i == n:
        print(0)

