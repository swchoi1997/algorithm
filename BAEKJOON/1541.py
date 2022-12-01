mod = input().split('-')

min_result = []
for i in mod:
    mod2 = i.split('+') 
    result = 0
    for j in mod2:
        result += int(j)
    
    min_result.append(result)

result1 = min_result[0]

for i in range(1,len(min_result)):
    result1 -= int(min_result[i])
    
print(result1)