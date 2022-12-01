
cut = ['=','-']

alpha = list(str(input()))

cnt = 0

for i in range(len(alpha)):
    if alpha[i] not in cut:
        if alpha[i] == 'j':
            if alpha[i-1] == 'n' or alpha[i-1] == 'l':
                continue
            else:
                cnt += 1
        else:
            cnt += 1 
    else:       
        if alpha[i-1] == 'z' and alpha[i-2] == 'd': #dz=
            cnt -= 1
        else:
            continue

print(cnt)


