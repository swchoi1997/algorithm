n = int(input())

if int(n ** (1/2)) == n **(1/2):
    print(1)
    exit()

for i in range(1, int(n ** (1/2)) + 1):
    if int((n - i ** 2) ** (1/2)) == (n - i ** 2) ** (1/2):
        print(2)
        exit()
for i in range(1, int(n ** (1/2)) + 1):
    for j in range(1, int((n - i ** 2) ** (1/2)) + 1):
        if int((n - i ** 2 - j ** 2) ** (1/2)) == (n - i ** 2 - j ** 2) ** (1/2):
            print(3)
            exit()

print(4)
exit()


    