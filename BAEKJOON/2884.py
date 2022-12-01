h, m = map(int, input().split())

new_m = m - 45
if new_m < 0:
    h -= 1
    new_m = (60 + m) - 45

    if h < 0:
        h = 23

print(h, new_m)