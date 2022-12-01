a = int(input())
list1 = []
for i in range(a):
    x, y = input().split()
    list1.append((int(x), list(y)))

for i in list1:
    for k in range(len(i[1])):
        print(i[1][k] * i[0], end = '')
    print()
