n = int(input())
num = list(map(int,input().split()))

check = [1] * n 

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            check[i] = max(check[i], check[j] + 1)

print(max(check))