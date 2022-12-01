import sys

while True:
    string = list(sys.stdin.readline().rstrip())
    if string == ['.']:
        break
        
    newstr = []
    for s in string:
        if s == '(' or s == '[':
            newstr.append(s)
        elif s == ')':
            if not newstr:
                newstr.append(s)
            else:
                if newstr[-1] == '(':
                    newstr.pop()
                elif newstr[-1] == '[':
                    newstr.append(s)
        elif s == ']':
            if not newstr:
                newstr.append(s)
            else:
                if newstr[-1] == '[':
                    newstr.pop()
                elif newstr[-1] == '(':
                    newstr.append(s)
    
    if not newstr:
        print('yes')
    else:
        print('no')
        
