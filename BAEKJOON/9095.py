import sys

n = int(input())

num = []
for _ in range(n):
    num.append(sys.stdin.readline().rstrip())

num = list(map(int, num))

for j in num:
    mem = [0] * (j + 1)
    if j < 3:
        print(j)
    elif j == 3:
        print(4)
    else:
        mem[1] = 1
        mem[2] = 2
        mem[3] = 4
        for i in range(4 , j + 1):
            mem[i] = mem[i - 1] + mem[i - 2] + mem[i - 3]
                
        print(mem[i])
