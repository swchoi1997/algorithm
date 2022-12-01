while True:
    num = []
    a, b, c = map(int, input().split())
    num.append(a)
    num.append(b)
    num.append(c)
    print(num)
    if a == 0 and b == 0 and c == 0:
        break
    
    num.sort()
    new_c = num.pop()

    if (num[0]**2) + (num[1]**2) == (new_c**2):
        print('right')
    else:
        print('wrong')