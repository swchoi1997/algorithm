#에라토스테네스의 체
def prime_list(m):
    a_num = [True] * (m + 1)
    a_num[0], a_num[1] = False, False
    for i in range(2, int(m**(1/2) + 1)):
        if a_num[i] == True:
            for j in range(i + i, m + 1, i):
                a_num[j] = False
    return a_num

n = int(input())
num = list(map(int, input().split()))

m = max(num)
prime_num = prime_list(m)

count = 0
for i in num:
    if prime_num[i] == True:
        count += 1

print(count)
