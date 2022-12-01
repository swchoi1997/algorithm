a = ['push', 'pop', 'size', 'empty', 'top']

import sys
input = sys.stdin.readline

n = int(input())

b = []
for _ in range(n):
    om1 = input().split()

    result =0
    if om1[0] == a[0]:
        b.append(om1[1])
    elif om1[0] == a[1]:
        if not b:
            print('-1')
        else:
            result = b.pop()
            print(result)
    elif om1[0] == a[2]:
        print(len(b))
    elif om1[0] == a[3]:
        if b:
            print('0')
        else:
            print('1')
    elif om1[0] == a[4]:
        if not b:
            print('-1')
        else:
            result = b.pop()
            print(result)
            b.append(result)

