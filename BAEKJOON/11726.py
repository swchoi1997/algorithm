n = int(input())
mem = [0] * (n + 1)

if n < 3:
    print(n % 10007)
    exit()
else:
    mem[1], mem[2] = 1, 2
    for i in range(3, n + 1):
        mem[i] = mem[i - 1] + mem[i -2]

    print(mem[n] % 10007)