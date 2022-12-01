from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int, input().rstrip().split())
number1 = list(input().rstrip())

cnt = 0

number2 = deque([])

for i in range(len(number1)):
    current = number1[i]
    if not number2:
        number2.append(current)
    else:
        if cnt != k: 
            while True:
                if cnt == k:
                    number2.append(current)
                    break 
                
                if number2[-1] >= current:
                    number2.append(current)
                    break
                else:
                    number2.pop()
                    cnt += 1

                if not number2:
                    number2.append(current)
                    break
   
        else:
            number2.append(current)

if cnt != k:
    for i in range(cnt, k):
        number2.pop()

for i in number2:
    print(i, end = '')
