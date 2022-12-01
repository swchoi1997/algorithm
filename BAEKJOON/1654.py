import sys
input = sys.stdin.readline

def min_num(m, sum_num, num):
    a = m
    while True:
        count =0
        aver = sum_num // m
        for i in num:
            count += i // aver
        if count >= a:
            return aver, count
        m += 1

def max_num(aver_num, num, new_m):
    while True:
        count = 0
        for i in num:
            count += i // aver_num
        if count != new_m:
            return aver_num - 1
        aver_num += 1

n, m = map(int, input().split())
num = []
num_sum = 0
for i in range(n):
    a = int(input())
    num_sum += a
    num.append(a)

aver_num, new_m = min_num(m, num_sum, num)

max_number = max_num(aver_num, num, new_m)

print(max_number)
    


