# 3
# 1212345
# 1212356
# 0033445

n = int(input())

student = []
for _ in range(n):
    student.append(list(str(input())))

for i in range(len(student[0])-1, -1, -1):
    check = []
    for j in range(n):
        student_number = student[j][i:]
        check.append(''.join(student_number))
    tmp = list(set(check))
    if len(tmp) == n:
        print(len(student[0]) - i)
        exit()