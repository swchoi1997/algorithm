from collections import deque

a = int(input())

for i in range(a):
    n, m = map(int, input().split())
    imp = deque(map(int, input().split()))
    wei = [h for h in range(n)] #순서
    
    count = 0
    while imp:
        max_num = max(imp)
        if imp[0] == max_num:
            count += 1
            imp.popleft()
            if wei[0] == m:
                print(count)
                break
            del wei[0]
        else:
            imp.append(imp.popleft())
            wei.append(wei[0])
            del wei[0]



