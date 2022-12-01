tects = [[[1,1,1,1]], [[1,1],[1,1]], [[1,1,1],[0,0,1]], [[1,1,1],[1,0,0]], [[1,1,0],[0,1,1]], [[0,1,1],[1,1,0]], [[1,1,1],[0,1,0]]]
# 대칭까지 생각해줘야하기때문에 case가 7개다
n, m = map(int,input().split())

stage = []
for i in range(n):
    stage.append(list(map(int,input().split())))


stage1 = [[0] * n for i in range(m)] # 90, 270
stage2 = [[0] * m for i in range(n)] # 180

def rotate1(stage): # 90 270 돌렸을때 
    for i in range(n):
        for j in range(m):
            stage1[j][(n - 1) - i] = stage[i][j]

def rotate2(stage): # 180 돌렸을때
    for i in range(n):
        for j in range(m):
            stage2[n - i - 1][m - j - 1]= stage[i][j]

def ts(i, j, a, b, stage, tect):
    result = 0
    for k in range(len(tect)):
        for l in range(len(tect[k])):
            x = i + k
            y = j + l

            if x >= a or y >= b:
                result = 0
                continue
            if tect[k][l] == 1:
                result += stage[x][y]
            else:
                continue
    return result

def maxi(stage):
    re_max = 0
    a = len(stage)
    for tect in tects:
        for i in range(len(stage)):
            b = len(stage[i])
            for j in range(b):
                re_max = max(re_max, ts(i,j,a,b,stage,tect))       
    return re_max


for i in range(4):
    if i == 1:
        rotate1(stage)
        result1 = maxi(stage1)
    elif i == 2:
        rotate2(stage)        
        result2 = maxi(stage2)
    elif i == 3:
        rotate1(stage2)        
        result3 = maxi(stage1)
    else:        
        result0 = maxi(stage)

print(max(result0, result1, result2, result3))

    
