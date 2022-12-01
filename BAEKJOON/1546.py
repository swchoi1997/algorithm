n = int(input())

getpoint = list(map(int, input().split()))
m = max(getpoint)

a = 0
for i in getpoint:    
    a += i / m * 100

average = a / len(getpoint)

print(average)