import sys
input = sys.stdin.readline

roma1 = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
roma2 = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}


def sumnum(num1):
    left = roma1[num1[0][0]]
    right = roma1[num1[1][0]]

    result = left + right
    for i in range(2):        
        crt = roma1[num1[i][0]]
        for j in range(1, len(num1[i])):
            if roma1[num1[i][j]] <= crt:
                result += roma1[num1[i][j]]
            else:
                result -= crt
                el1 = num1[i][j-1] + num1[i][j]
                result += roma2[el1]
            
            crt = roma1[num1[i][j]]

    return result


num1 = []
for _ in range(2):
    num1.append(list(map(str, input().rstrip())))

result1 = sumnum(num1)
result1list = list(map(int, str(result1)))

result2 = ''
t = len(result1list)
n = len(result1list)

for i in reversed(range(n)):
    point = result1list[t-(i + 1)]
    if i == 3:
        result2 += 'M' * point
    elif i == 2:
        if point == 9:
            result2 += 'CM'
        elif point == 4:
            result2 += 'CD'
        else:
            if point >= 5:
                result2 += 'D'
            result2 += 'C' * (point % 5)
    elif i == 1:
        if point == 9:
            result2 += 'XC'
        elif point == 4:
            result2 += 'XL'
        else:
            if point >= 5:
                result2 += 'L'
            result2 += 'X' *(point % 5)
    elif i == 0:
        if point == 9:
            result2 += 'IX'
        elif point == 4:
            result2 += 'IV'
        else:
            if point >= 5:
                result2 += 'V'
            result2 += 'I' *(point % 5)
        
print(result1)
print(result2)


#---------------------------------------------------------------------
# import sys
# roma1 = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
# roma2 = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90 , 'CD' : 400, 'CM' : 900}
# input = sys.stdin.readline

# num1 = list(map(str, input().rstrip()))
# num2 = list(map(str, input().rstrip()))

# left, right = roma1[num1[0]], roma1[num2[0]]
# crt1 = roma1[num1[0]]
# el1 = ''
# cnt1 = crt1
# for i in range(1, len(num1)):
#     if roma1[num1[i]] < crt1:
#         cnt1 += roma1[num1[i]]
#     elif roma1[num1[i]] == crt1:
#         cnt1 += roma1[num1[i]]
#     else:
#         cnt1 -= crt1
#         el1 = num1[i - 1] + num1[i]
#         cnt1 += roma2[el1]

#     crt1 = roma1[num1[i]]
    

# crt2 = roma1[num2[0]]
# el2 = ''
# cnt2 = crt2
# for i in range(1, len(num2)):
#     if roma1[num2[i]] < crt2:
#         cnt2 += roma1[num2[i]]
#     elif roma1[num2[i]] == crt2:
#         cnt2 += roma1[num2[i]]
#     else:
#         cnt2 -= crt2
#         el2 = num2[i - 1] + num2[i]
#         cnt2 += roma2[el2]

#     crt2 = roma1[num2[i]]
    
    
# print(cnt1 + cnt2)

