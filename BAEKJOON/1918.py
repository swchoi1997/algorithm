import sys
from collections import deque
input = sys.stdin.readline

def mdpm(tmp, s, val):
    global result
    if not s:
        s.append([tmp, val])
    else:
        while True:
            if not s: break
            if s[-1][1] > val: break
            if s[-1][1] <= val:
                a, b = s.pop()
                result += a
        s.append([tmp, val])

def close_bracket(tmp, s):
    global result
    while True:
        if not s: break
        if s[-1][0] == "(":
            s.pop()
            break
        a, b = s.pop()
        result += a

def postfix(pf):
    global result
    s = [] # stack
    while pf:
        tmp = pf.popleft()
        if tmp == "*" or tmp == "/": mdpm(tmp, s, 1)
        elif tmp == "+" or tmp == "-": mdpm(tmp, s, 2)
        elif tmp == "(": s.append([tmp, 3])
        elif tmp == ")": close_bracket(tmp, s)
        else: result += tmp
    if s:
        while s:
            a, b = s.pop()
            result += a
    
pf  = deque(list(map(str, input().rstrip())))
result = ''
postfix(pf)
print(result)

########################################################################################
## 후위표기식 구하는 법                                                                    ##
## 1. 피연산자가 나오면 그냥 출력한다.                                                        ##
## 2. 연산자가 나오고 스택이 비어있으면 그 값과 우선순위를 스택에 넣어준다.                            ##
## 3. 스택이 비어있지않으면 현재 연산자의 우선순위보다 스택[-1] 번쨰 있는 값의 우선순위가                 ##
##    높거나 같으면(내가 코딩한 방식에서는 값이 작거나 같으면) pop해서 출력해주고                       ##
##    자기 자신은 스택에 넣어준다.( 자기보다 우선순위가 낮은 연산자가 보일 때 까지 pop 해줌)              ##
##    * 스택이 비어있으면 멈춤                                                              ##
## 4. "(" 여는괄호가 나오면 그냥 스택에 넣어준다.                                               ##
## 5. ")" 닫는 괄호가 나오면 "(" 여는 괄호가 나올 떄까지 pop 하여 출력해준다. "(" 여는 괄호는 pop만 해줌 ##
########################################################################################

#################처음에 푼게 복잡해서 보기 쉽게 바꿈 ###################

# postfix = deque(list(map(str, input().rstrip())))

# stack1 = []
# result = ''
# while postfix:
#     tmp = postfix.popleft()

#     if tmp == "*" or tmp == "/":
#         if not stack1:
#             stack1.append([tmp, 1])
#         else:
#             while True:
#                 if not stack1:
#                     break
#                 if stack1[-1][1] > 1:
#                     break
#                 if stack1[-1][1] <= 1:
#                     a, b = stack1.pop()
#                     result += a
#             stack1.append([tmp, 1])

#     elif tmp == "+" or tmp == "-":
#         if not stack1:
#             stack1.append([tmp, 2])
#         else:
#             while True:
#                 if not stack1:
#                     break
#                 if stack1[-1][1] > 2:
#                     break
#                 if stack1[-1][1] <= 2:
#                     a, b = stack1.pop()
#                     result += a
#             stack1.append([tmp, 2])

#     elif tmp == "(":
#         stack1.append([tmp, 3])
#     elif tmp == ")":
#         while True:
#             if not stack1:
#                 break
#             if stack1[-1][0] == "(":
#                 stack1.pop()
#                 break
#             a, b = stack1.pop()
#             result += a
#     else:
#         result += tmp
# if stack1:
#     while stack1:
#         a, b = stack1.pop()
#         result += a
# print(result)