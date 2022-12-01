# add, remove, check, toggle, all empty

import sys
input = sys.stdin.readline

empty_input = dict()
all_input = {1:1, 2:2, 3:3, 4:4, 5:5 ,6:6, 7:7, 8:8, 9:9, 10:10,
            11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20}

m = int(input())
s = dict()
for _ in range(m):
    a = list(map(str,input().rstrip().split()))

    if a[0] == 'all':
        s = all_input
    elif a[0] == 'empty':
        s = empty_input
    else:
        b = int(a[-1])
        if a[0] == 'add':
            if b not in s :s[b] = b
        elif a[0] == 'remove':
            if b in s : del s[b]
        elif a[0] == 'check':
            print('1') if b in s else print('0')
        elif a[0] == 'toggle':
            if b in s : del s[b]
            else : s[b] = b
