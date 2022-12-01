# 4949 균현잡힘 세상

while True:
    string = input()
    if string == '.':
        break
    newstr = []
    string = list(string)
    for i in string:
        if i == '[' or i == '(' or i == ')' or i == ']':
            newstr.append(i)
    if len(newstr) == 0:
        print('yes')
        continue
    newstr2 = []
    for i in newstr:
        if i == '[' or i == '(':
            newstr2.append(i)
        else:
            if len(newstr2) == 0:
                newstr2.append(i)
                continue
            if newstr2[-1] == '[' and i == ']':
                newstr2.pop()
            elif newstr2[-1] == '(' and i == ')':
                newstr2.pop()
            elif newstr2[-1] == '(' and i == ']':
                newstr2.append(i)
            elif newstr2[-1] == '[' and i == ')':
                newstr2.append(i)
        
    if len(newstr2) == 0:
        print('yes')
    else:
        print('no')
