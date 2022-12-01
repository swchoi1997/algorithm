n = int(input())

if 0 < n <= 9: 
    print(1 * n)
    exit()
elif 10 <= n < 100:
    print(1 * 9 + 2 *(n - 9))
    exit()
else:
    result = 0
    for i in range(1, len(str(n)) + 1):
        if i == len(str(n)):
            result += i * (n - ((10 ** (i - 1)) - 1))
        else:
            result += 9 * i * (10 ** (i - 1))

    print(result)

            
