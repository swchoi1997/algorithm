a = list(map(int, input().split()))
count = 0
for i in range(len(a) - 1):
    if a[i + 1] == (a[i] + 1):
        count += 1
    elif a[i + 1] == (a[i] - 1):
        count -= 1

if count == 7:
    print('ascending')
elif count == -7:
    print('descending')
else:
    print('mixed')