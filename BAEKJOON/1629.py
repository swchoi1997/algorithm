import sys
input = sys.stdin.readline
a, b, c = map(int,input().split())

def dq(a,b):
    if b == 1:
        return a % c
    
    else:
        tmp = dq(a, b //2)
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(dq(a,b))