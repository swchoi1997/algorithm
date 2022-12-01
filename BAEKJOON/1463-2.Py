num = int(input())

check = [0] * (num + 1)

for i in range(2, len(check)):
    check[i] = check[i-1] + 1
    if i % 2 == 0:
        check[i] = min(check[i], check[i // 2] + 1)
    if i % 3 == 0:
        check[i] = min(check[i], check[i // 3] + 1)
    
print(check[num])
    
