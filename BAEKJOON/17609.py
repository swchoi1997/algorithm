import sys
input =sys.stdin.readline

def palin2(string, x, y):
    while x < y:
        if string[x] == string[y]:
            x += 1
            y -= 1
        else:
            return False
    return True
def palin1(string):
    x = 0
    y = len(string) - 1
    while x < y:
        if string[x] == string[y]:
            x += 1
            y -= 1
        else:
            a = palin2(string, x + 1, y)
            b = palin2(string, x, y - 1)
            if a or b:
                return 1
            else:
                return 2
    return 0
    
t = int(input())
for _ in range(t):
    string = list(map(str,input().rstrip()))
    print(palin1(string))
    