import sys 
input = sys.stdin.readline

n = int(input())
initCar = dict()
for i in range(n):
    car = input().rstrip()
    initCar[car] = i + 1

finalCar = []
for i in range(n):
    car = input().rstrip()
    finalCar.append(initCar[car])

checkCar = [0 for i in range(n)]


for i in range(1, n):
    std = finalCar[i]
    for j in range(i):
        if checkCar[j] == 0 and finalCar[j] > std:
            checkCar[j] = 1


print(sum(checkCar))