from collections import deque
import re
t = int(input())


for _ in range(t):
    rd = list(input())
    a = int(input())
    number = input()
    number = number.replace('[','')
    number = number.replace(']','')

    number2 = deque(re.split(',', number))

    TF = True
    check = True
    cnt = 0
    for i in rd:
        if i == 'D':
            a -= 1
            if a < 0:
                TF = False
                break
            else:                
                if check == True:
                    number2.popleft()
                else:
                    number2.pop()
        else:
            check = not check
            # if check == True:
            #     check = False
            # else:
            #     check = True

    number2 = list(number2)
    if TF == True and a == 0:
        print('[]')
    elif TF == False:
        print('error')
    else:
        if check == False:
            number2.reverse()
        print('[' + ','.join(number2) + ']')
        
        

# from collections import deque
# import re
# t = int(input())


# for _ in range(t):
#     rd = list(input())
#     a = int(input())
#     number = input()
#     number = number.replace('[','')
#     number = number.replace(']','')

#     number2 = deque(re.split(',', number))

#     TF = True
#     cnt = 0
#     for i in rd:
#         if i == 'D':
#             a -= 1
#             if a < 0:
#                 TF = False
#                 break
#             else:
#                 if cnt % 2 == 1:
#                     number2.reverse()
#                     number2.popleft()
#                     cnt = 0
#                 else:
#                     number2.popleft()
#         else:
#             cnt += 1

    
#     if TF == True and a == 0:
#         print('[]')
#     elif TF == False:
#         print('error')
#     else:
        
        # print('[', end = '')
        # for i in range(len(number2)):
        #     print(number2[i],end = '')
        #     if i == len(number2) - 1:
        #         print(']')
        #     else:
        #         print(',', end = '')
        