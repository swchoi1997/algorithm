def is_prime_num(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

n = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    if i == 1:
        continue
    if i != 1 and  i <= 3:
        count += 1
    if i > 3:
        if is_prime_num(i) == True:
            count += 1

print(count)

