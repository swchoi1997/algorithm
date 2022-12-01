def bs(z, start, end, x, y):
    result = 1e20
    while start <= end:
        mid = (start + end) // 2

        new_z = 100 * (y + mid) // (x + mid)
        
        if new_z > z:
            result = min(result, mid)
            end = mid -1
        else:
            start = mid + 1
        
    return result

x, y = map(int,input().split())

init_z = (100 * y // x)


if init_z >= 99:
    print(-1)
else:
    print(bs(init_z, 1, x, x, y))