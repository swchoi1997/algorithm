num1 = []
for _ in range(10):
    a = input()
    num1.append(int(a))

num2 = [0] * 42
for i in num1:
    b = i % 42
    num2[b] += 1

count =0
for i in num2:
    if i >= 1:
        count +=1

print(count)