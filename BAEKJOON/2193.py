n = int(input())

array = [0] * (n)

if n == 1 or n == 2:
    print(1)

elif n >= 3:
    array[0] = 1
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i-1] + array[i-2]
    print(array[-1])