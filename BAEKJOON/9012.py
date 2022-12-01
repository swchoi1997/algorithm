n = int(input())
ps = []
for i in range(n):
    psps = input()
    ps.append(list(psps))

checkps = []
count = 0
for i in ps:
    for j in range(len(i)):
        if i[j] == '(':
            checkps.append(i[j])
            count += 1
        elif i[j] == ')':
            if checkps:
                if checkps[count - 1] == '(':
                    checkps.pop()
                    count -= 1
                else:
                    checkps.append(i[j])
                    count += 1
            else:
                checkps.append(i[j])
                count += 1
    if checkps:
        print('NO')
    else:
        print('YES')
    checkps.clear()
    count = 0