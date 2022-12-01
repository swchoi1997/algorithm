import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))
oper = list(map(int,input().split())) # + - * /

tmpMax = -1e20
tmpMin = 1e20
check = []

def dfs():
    global tmpMax, tmpMin
    if sum(oper) == 0:
        result = pmmd(check)
        tmpMax = max(tmpMax, result)
        tmpMin = min(tmpMin, result)
        return 
    for i in range(4):
        if oper[i] != 0:
            oper[i] -= 1
            check.append(i)
            dfs()
            oper[i] += 1
            check.pop()

def pmmd(check):
    result = numbers[0]    
    for i in range(1, len(numbers)):
        if check[i - 1] == 0:
            result += numbers[i]
        elif check[i - 1] == 1:
            result -= numbers[i]
        elif check[i - 1] == 2:
            result *= numbers[i]
        else:
            if result < 0:
                result = -result // numbers[i]
                result = -result
            else:
                result = result // numbers[i]

    return result

dfs()

print(tmpMax)
print(tmpMin)





