import sys
input = sys.stdin.readline

def bs(bluelay, a, b):
    result = sys.maxsize
    while a <= b:
        mid = (a + b) // 2
        tmp = 0
        cnt = 1
        for i in range(len(bluelay)):
            tmp += bluelay[i]
            if tmp > mid:
                cnt+= 1
                tmp = 0
                tmp += bluelay[i]
        if cnt > m:
            a = mid + 1
        elif cnt <= m:
            result = min(result, mid)
            b = mid - 1

    return result
        
    

n, m = map(int,input().split())
bluelay = list(map(int,input().split()))

print(bs(bluelay, max(bluelay), sum(bluelay)))