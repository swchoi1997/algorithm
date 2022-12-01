result = 0
for _ in range(5):
    grade = int(input())
    if grade <= 40:
        grade = 40
    result += grade

print(result // 5)