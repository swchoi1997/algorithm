import sys
input = sys.stdin.readline

def rotate_str(finalStr):
    for i in range(len(finalStr) // 2):
        tmp = finalStr[i]
        finalStr[i] = finalStr[len(finalStr) - i - 1]
        finalStr[(len(finalStr) - i - 1)] = tmp

    
initStr = input().rstrip()
finalStr = list(input().rstrip())

while len(initStr) != len(finalStr):
    if finalStr[-1] == 'A':
        finalStr.pop()
    else:
        finalStr.pop()
        rotate_str(finalStr)

checkStr = "".join(finalStr)

if initStr == checkStr: print(1)
else: print(0)