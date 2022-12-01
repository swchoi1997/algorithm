m = int(input())
for i in range(m):
    h, w ,n =  map(int, input().split())
    
    a, b = 0, 0
    if n % h == 0:
        a = h * 100
        b = n // h
    else:
        a = (n % h) * 100
        b = n // h + 1
    r_num = 0
    r_num = a + b
    print(r_num)
