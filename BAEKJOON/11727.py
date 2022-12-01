a = int(input())
if a == 1:
    print(1)
    exit()
if a == 2:
    print(3)
    exit()
if a == 3:
    print(5)
    exit()

n = [0] * a
n[0] = 1
n[1] = 3
n[2] = 5

for i in range(3, a):
    n[i] = n[i-1] + 2* n[i-2]

print(n[-1] % 10007)