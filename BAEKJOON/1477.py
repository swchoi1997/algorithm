import sys
input = sys.stdin.readline

n,h = map(int,input().split())

lo = []
he = []
for i in range(n):
    a = int(input())
    if i % 2 == 0:
        lo.append(a)
    else:
        he.append(a)

lo.sort()
he.sort()

def bs(target, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+ end) // 2

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return len(arr) - end - 1


result = int(10e9)
cnt = 1
for i in range(h):
    lo_bs = bs(i  + 0.5 ,lo)
    he_bs = bs(h - i  - 0.5,he)

    tmp = lo_bs + he_bs

    if tmp < result:
        cnt = 1
        result = tmp
    elif tmp == result:
        cnt += 1

print(result, cnt)

    

