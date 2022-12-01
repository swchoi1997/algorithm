cnt = 1
while True:
    l, p, v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        exit()
    
    result  = (v // p) * l

    if v % p <= l:
        result += v % p
    else:
        result += l

    print(f'Case {cnt}: {result}')
    cnt += 1