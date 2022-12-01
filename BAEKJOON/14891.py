wheel = [list(map(int,input())) for _ in range(4)]

def checkSideWheel(wheelNum):
    check = [False, False, False, False]
    if wheelNum == 1:
        check[wheelNum - 1] = True # 본인은 회전해야하니가 True
        if wheel[0][2] != wheel[1][6]: # 다르면 회전해야하니까
            check[1] = True
        else:
            return check
        if wheel[1][2] != wheel[2][6]:
            check[2] = True
        else:
            return check
        if wheel[2][2] != wheel[3][6]:
            check[3] = True
        else:
            return check
        return check

    elif wheelNum == 4:
        check[wheelNum - 1] = True # 본인은 회전해야하니가 True
        if wheel[2][2] != wheel[3][6]: # 다르면 회전해야하니까
            check[2] = True
        else:
            return check
        if wheel[1][2] != wheel[2][6]:
            check[1] = True
        else:
            return check    
        if wheel[0][2] != wheel[1][6]:
            check[0] = True
        else:
            return check
        return check

    elif wheelNum == 2:
        check[wheelNum - 1] = True # 본인은 회전해야하니가 True
        if wheel[0][2] != wheel[1][6]:
            check[0] = True
        if wheel[1][2] != wheel[2][6]:
            check[2] = True
        else:
            return check
        if wheel[2][2] != wheel[3][6]:
            check[3] = True
        return check
    else:
        check[wheelNum - 1] = True # 본인은 회전해야하니가 True
        if wheel[2][2] != wheel[3][6]:
            check[3] = True
        if wheel[1][2] != wheel[2][6]:
            check[1] = True
        else:
            return check
        if wheel[0][2] != wheel[1][6]: # 다르면 회전해야하니까
            check[0] = True
        return check

def rotate(num):
    tmp = wheel[num -1][-1]
    for i in range(7, 0, -1):
        wheel[num -1][i] = wheel[num - 1][i - 1]
    wheel[num - 1][0] = tmp

def reverseRotate(num):
    tmp = wheel[num -1][0]
    for i in range(7):
        wheel[num -1][i] = wheel[num - 1][i + 1]
    wheel[num - 1][-1] = tmp

def rotateSideWheel(wheelNum, dir, check):
    if dir == 1:
        rotate(wheelNum)
        if wheelNum == 1:
            if check[wheelNum] == True:
                reverseRotate(wheelNum + 1)
            else: return
            if check[wheelNum + 1] == True:
                rotate(wheelNum + 2)
            else: return
            if check[wheelNum + 2] == True:
                reverseRotate(wheelNum + 3)


        elif wheelNum == 2:
            if check[wheelNum - 2] == True:
                reverseRotate(wheelNum - 1)
            if check[wheelNum] == True:
                reverseRotate(wheelNum + 1)
            else: return
            if check[wheelNum + 1] == True:
                rotate(wheelNum + 2)

        elif wheelNum == 3:
            if check[wheelNum] == True:
                reverseRotate(wheelNum + 1)
            if check[wheelNum - 2] == True:
                reverseRotate(wheelNum - 1)
            else: return
            if check[wheelNum - 3] == True:
                rotate(wheelNum - 2)

        else:
            if check[wheelNum - 2] == True:
                reverseRotate(wheelNum -1)
            else: return
            if check[wheelNum - 3] == True:
                rotate(wheelNum -2)
            else: return
            if check[wheelNum - 4] == True:
                reverseRotate(wheelNum -3)

    else:
        reverseRotate(wheelNum)
        if wheelNum == 1:
            if check[wheelNum] == True:
                rotate(wheelNum + 1)
            else: return
            if check[wheelNum + 1] == True:
                reverseRotate(wheelNum + 2)
            else: return
            if check[wheelNum + 2] == True:
                rotate(wheelNum + 3)


        elif wheelNum == 2:
            if check[wheelNum - 2] == True:
                rotate(wheelNum - 1)
            if check[wheelNum] == True:
                rotate(wheelNum + 1)
            else: return
            if check[wheelNum + 1] == True:
                reverseRotate(wheelNum + 2)

        elif wheelNum == 3:
            if check[wheelNum] == True:
                rotate(wheelNum + 1)
            if check[wheelNum - 2] == True:
                rotate(wheelNum - 1)
            else: return
            if check[wheelNum - 3] == True:
                reverseRotate(wheelNum - 2)

        else:
            if check[wheelNum - 2] == True:
                rotate(wheelNum -1)
            else: return
            if check[wheelNum - 3] == True:
                reverseRotate(wheelNum -2)
            else: return
            if check[wheelNum - 4] == True:
                rotate(wheelNum -3)


def rotate_wheel(wheelNum, dir):
    
    checkSide = checkSideWheel(wheelNum)
    rotateSideWheel(wheelNum, dir, checkSide)

t = int(input())
for _ in range(t):
    wheelNum, dir = map(int,input().split())
    rotate_wheel(wheelNum, dir)
result = 0
a = 1
for i in wheel:
    if i[0] == 1:
        result += a
    a *= 2
print(result)


# 11001110
# 10000101
# 01111110
# 01101111
# 4
# 2 -1
# 2 -1
# 2 1
# 2 1


# 01100110
# 10001111
# 00011000
# 10111000
# 3
# 3 -1
# 3 1
# 1 1


# 10111000
# 10100110
# 11000010
# 00001100
# 8
# 1 -1
# 4 1
# 1 1
# 1 -1
# 1 1
# 2 1
# 2 -1
# 4 1


# 01100001
# 01100001
# 01100001
# 00000000
# 1
# 4 1
