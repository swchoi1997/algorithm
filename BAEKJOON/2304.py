n = int(input())

max_h = 0
col=[]
for _ in range(n):
    l, h = map(int,input().split())
    if h > max_h:
        max_h = h
    col.append([l,h])

if n == 1:
    print(col[0][1])
    exit()

col = sorted(col, key = lambda x : x[0])

result1 = 0
highindex1 = 0
tmpl, tmph = 0, 0
for i in range(len(col)): 
    if i == 0:
        tmpl, tmph = col[i][0], col[i][1]
    else:
        if tmph < col[i][1]:
            result1 += (col[i][0] - tmpl) * tmph
            tmpl, tmph = col[i][0], col[i][1]
        else:
            continue    

    if col[i][1] == max_h:
        highindex1 = col[i][0]
        result1 += max_h
        break

result2 = 0
highindex2 = 0
tmpl1, tmph1 = 0,0
for i in range(len(col) - 1, 0, -1):
    if i == len(col)- 1:
        tmpl1, tmph1 = col[-1][0], col[-1][1]
    else:
        if tmph1 < col[i][1]:
            result2 += (tmpl1 - col[i][0]) * tmph1
            tmpl1, tmph1 = col[i][0], col[i][1]
        else:
            continue    

    if col[i][1] == max_h: 
        highindex2 = col[i][0]
        break
result = 0
if highindex1 != highindex2:
    result += (highindex2 - highindex1) * max_h
# print(result1, result2, result)
print(result1 + result2 + result)
# 5
# 1 4
# 2 5
# 3 6
# 4 5
# 5 4 

# 7
# 2 4
# 11 4
# 15 10
# 4 6
# 5 3
# 8 10
# 13 6

# 5
# 2 4
# 4 6
# 5 3
# 8 6
# 10 2

# 6
# 3 4
# 2 5
# 6 6
# 1 6
# 5 5
# 4 4

# 6
# 1 5
# 2 6
# 3 5
# 4 4
# 5 6
# 6 5


# 5
# 13 4
# 6 5
# 4 3
# 11 3
# 9 5

# 5
# 3 5
# 6 2
# 7 1
# 4 6
# 9 5
