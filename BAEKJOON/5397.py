import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    keylog = list(map(str, input().rstrip()))
    l = []
    r = []
    for k in keylog:
        if k == '>':
            if r: l.append(r.pop())
        elif k == '<':
            if l: r.append(l.pop())
        elif k == '-':
            if l: l.pop()
        else:
            l.append(k)


    print(''.join(l) + ''.join(reversed(r)))


# 1
# <<BP<A>>Cd-
