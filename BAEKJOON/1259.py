num = []
while True:
    a = input()
    if a == '0':
        break
    num.append(list(a))

check_data = []
for i in num:
    check = ''
    for j in range(len(i) // 2):
        if i[j] == i[len(i) -(j + 1)]:
            check = 'yes'
        else:
            check = 'no'
    check_data.append(check)

for i in check_data:
    print(i)


# while True:
#     a = input()
#     if a == '0':
#         break
    
#     if a == a[::-1]:
#         print('yes')
#     elif a != a[::-1]:
#         print('no')




