n, m = map(int, input().split())

num = [True] * (m + 1)
num[0],num[1] = False, False

for i in range(2, int(m**(1/2) + 1)):
    for j in range(i+i, m + 1, i):
        num[j] = False

for i in range(n, m + 1):
    if num[i] == True:
        print(i)
