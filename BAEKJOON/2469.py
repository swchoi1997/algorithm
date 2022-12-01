import sys
input = sys.stdin.readline

def exchange(tmp):
    for i in range(len(tmp)):
        if tmp[i] == "-":
            tmp1 = startStr[i]
            startStr[i] = startStr[i + 1]
            startStr[i + 1] = tmp1

def exchange2(tmp):
    for i in range(len(tmp)):
        if tmp[i] == "-":
            tmp1 = finalStr[i]
            finalStr[i] = finalStr[i + 1]
            finalStr[i + 1] = tmp1

k = int(input())
n = int(input())

startStr = [i for i in range(1, k + 1)]
finalStr = list(map(str, input().rstrip()))
for i in range(k):
    finalStr[i] = ord(finalStr[i]) - 64

#after question mark
afterQM = []
qCheck = False
for _ in range(n):
    tmp = input().rstrip()
    if not qCheck:
        exchange(tmp)
    else:
        afterQM.append(tmp)

    if tmp[0] == "?":
        qCheck = not qCheck

for i in range(len(afterQM) - 1, - 1, -1):
    exchange2(afterQM[i])

result = ''
for i in range(k - 1):
    if startStr[i] == finalStr[i]:
        result += "*"
    elif startStr[i] != finalStr[i]:
        if startStr[i] == finalStr[i + 1] and startStr[i + 1] == finalStr[i]:
            result += "-"
        else:
            if len(result) != 0:
                if result[-1] == "-":
                    result += "*"
                    continue
                else:
                    print("x" * (k - 1))
                    exit()
            else:
                print("x" * (k - 1))
                exit()

print(result)
            

    