n, m = map(int,input().split())
num = [i for i in range(n + 1)]
num1 = [i for i in range(n + 1)]

for i in range(2, m + 1):
    num[i] *= num[i - 1]
for j in range(n - m + 2, n + 1):
    num1[j] *= num1[j - 1]

# print(num)
# print(num1)
# print(num1[-1], num[m])
print(num1[-1]// num[m])