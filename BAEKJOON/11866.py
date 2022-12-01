from collections import deque
n,m = map(int,input().split())

arr = deque([(i+ 1) for i in range(n)])

cnt1 = 1
cnt2 = 0
print('<', end = '')
while True:
    a = arr.popleft()
    cnt2 += 1 
    if cnt2 == m:
        if cnt1 < n:
            print(a, end = ', ')
            cnt1 += 1
        else:
            print(a, end = '')
            break
        cnt2 = 0
    else:
        arr.append(a)
print('>')
