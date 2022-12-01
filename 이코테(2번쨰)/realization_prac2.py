import re

list1 = input()

numbers = re.findall('\d', list1)
newlists = list(re.sub(r'[0-9]', '',list1))

newlists.sort()

sum_num = 0
for i in range(len(numbers)):
    sum_num += int(numbers[i])

for i in newlists:
    print(i, end ='')
print(sum_num)