import sys
input = sys.stdin.readline

def csize(m, num, start, end):
    result = 0
    while start <= end:
        cnt = 0
        
        mid = (start + end) // 2
        for i in num:
            cnt += i // mid

        if cnt >= m:
            result = mid
            start = mid + 1
        else:
            end = mid -  1
    return result

n, m = map(int, input().split())
num = []
for i in range(n):
    a = int(input())
    num.append(a)
    
cutsize = csize(m, num, 1, max(num))
print(cutsize)