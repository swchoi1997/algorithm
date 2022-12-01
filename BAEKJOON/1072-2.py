x, y = map(int,input().split())
z = 100 * y // x


if z >= 99:
    print(-1)
else:
    start,end = 1, x
    result = 1e20
    while start <= end:
        mid = (start + end) // 2

        tmp = 100 * (y + mid) // (x + mid)

        if tmp > z:
            result = min(result, mid)
            end = mid - 1
        else:
            start= mid + 1
    
    print(result)
