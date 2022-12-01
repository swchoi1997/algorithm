import sys
from collections import deque
input = sys.stdin.readline

word = deque(list(map(str,input().rstrip())))

result = ''
word2 = deque([])
TF = False
 
while word:
    curt = word.popleft()
    if curt == '<':
        TF = True
        for _ in range(len(word2)):
            result += word2.pop()
        word2.append(curt)
        
    elif curt == '>':
        TF = False
        word2.append(curt)
        for _ in range(len(word2)):
            result += word2.popleft()

    elif curt == ' ' and TF == True:
        word2.append(curt)

    elif curt == ' ' and TF == False:
        for _ in range(len(word2)):
            result += word2.pop()
        result += curt

    else:
        word2.append(curt)

if len(word2) > 0:
    if TF == True:
        for _ in range(len(word2)):
            result += word2.popleft()
    else:
        for _ in range(len(word2)):
            result += word2.pop()
    

print(result)


##########이건 뒤집는 코드인데 pop 이랑 popleft 이용하면됨######
# def reversedword(word2):
#     for i in range(len(word2) // 2):
#         tmp = word2[i]
#         word2[i] = word2[len(word2) - i - 1]
#         word2[len(word2) - i - 1] = tmp




############아래는 일단 뒤집기 위한 아이디어############3
#     cut = word.popleft()
      
#     if cut == ' ':
#         # reversedword(word2)
#         for _ in range(len(word2)):
#             result += word2.pop()
#         result += ' '
#     else:
#         word2.append(cut)


# for _ in range(len(word2)):
#     result += word2.pop()

# print(result)

    
