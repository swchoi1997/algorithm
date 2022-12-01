mod = list(input().split('-'))

result = 0
for i in range(len(mod)):
    mod2 = mod[i].split('+')
    val = 0
    for j in mod2:
        val += int(j)
    if i == 0:
        result += val
    else:
        result -= val

print(result)
            