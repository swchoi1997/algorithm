a = [[1,2,3],[4,5,6],[7,8,9]]
b = [x[:] for x in a]

b[0][0] = 0

for i in a:
    print(i)

for i in b:
    print(i)