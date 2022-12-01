import sys
input = sys.stdin.readline

n = int(input())
check = [0] * 10001

num_max = 0
for _ in range(n):
    num1 = int(input())
    check[num1] += 1
    #num_max = max(num_max, num1)

for i in range(1, len(check)):
    if check[i] == 0:
        continue
    else:
        for _ in range(check[i]):
            print(i)
