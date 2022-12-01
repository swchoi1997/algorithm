import sys
from collections import deque

input = sys.stdin.readline

bracket = list(input().rstrip())

bracket1 = deque(bracket)
array = []

for i in range(len(bracket1)):
    cnt = 0
    a = bracket1.popleft()

    if not array:
        array.append(a)
        if array[-1] == ']' or array[-1] == ')':
            print(0)
            exit()
    
    else:
        if a == '[' or a == '(':
            array.append(a)

        elif a == ')':
            while len(array) != 0:
                top = array.pop() 
                if top == '[': 
                    print(0)
                    exit()
                elif top == '(': 
                    if cnt == 0:    
                        array.append(2)
                    else:
                        array.append(2 * cnt)
                    break
                else:
                    cnt += top 

        elif a == ']':
            while len(array) != 0:
                top = array.pop()
                if top == '(':
                    print(0)
                    exit()
                elif top == '[':
                    if cnt == 0:
                        array.append(3)
                    else:
                        array.append(3 * cnt)
                    break
                else:
                    cnt += top
b = ['[',']','(',')']

for i in array:
    if i in b:
        print(0)
        exit()
print(sum(array))

