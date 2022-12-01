a = int(input())
b = int(input())
c = int(input())
prod = a * b * c

number_list = list(str(prod))
count_list= [0] * 10

for i in number_list:
    count_list[int(i)] += 1
for i in count_list:
    print(i)