from collections import deque

n = int(input())
num_list = [i for i in range(1, n + 1)]
num = deque()
for i in num_list:
    num.append(i)
if n > 1:
    while True:
        num.popleft()
        n -= 1    
        if n == 1:
            break
        a = num.popleft()
        num.append(a)

print(num.popleft())

    
