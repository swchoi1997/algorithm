number_set = [0] * 10

room_number = list(map(int,input()))

for i in room_number:
    if i == 6 or i == 9:
        number_set[9] += 1
        continue
    number_set[i] += 1

if number_set[9] % 2 == 0:
    number_set[9] //= 2
else: 
    number_set[9] = number_set[9] // 2 + 1

print(max(number_set))