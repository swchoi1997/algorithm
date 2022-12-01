import sys
input = sys.stdin.readline

def monsplit(mon, m, start, end):
    while start <= end:
        mid = (start + end) // 2

        totalmoney = 0
        for i in mon:
            totalmoney += min(i, mid)

        if m >= totalmoney:
            start = mid + 1
        else:
            end = mid - 1
    return end
 
n = int(input())
mon = list(map(int,input().split()))
m = int(input())

mon.sort()
if (sum(mon) // n) > mon[-1]:
    print(mon[-1])
else:
    print(monsplit(mon, m, 1, max(mon)))
    