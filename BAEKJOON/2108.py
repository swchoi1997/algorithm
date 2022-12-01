from collections import Counter
import sys
input = sys.stdin.readline

def aver(n, sum_num): #산술평균    
    aver = sum_num / n
    aver2 = sum_num // n
    if aver - aver2 >= 0.5:
        return aver2 + 1
    else:
        return aver2
def midvalue(n, num): #중앙값
    if len(num) == 1:
        return num[0]
    else:
        return num[len(num) // 2]

def maxfreg(n, num):
    if len(num) == 1:
        return num[0]
    else:
        num2 = Counter(num)
        order = num2.most_common()
        maxinum = order[0][1]

        num3 = []
        for i in order:
            if i[1] == maxinum:
                num3.append(i[0])
        if len(num3) == 1:
            return num3[0]
        elif len(num3) >= 2:
            return num3[1]


def ran(num):
    return max(num) - min(num)

n = int(input())

num = []
sum_num = 0
for i in range(n):
    a = int(input())
    sum_num += a
    num.append(a)
num.sort()
print()
print(aver(n, sum_num))
print(midvalue(n, num))
print(maxfreg(n, num))
print(ran(num))



