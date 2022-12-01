n = int(input())
words = []
for _ in range(n):
    tmp = list(str(input()))
    words.append(list(set(tmp)))

fword = words[0]
d = dict()
for i in fword:
    if d.get(i) is None:
        d[i] = 1

result = 0
for i in range(1, len(words)):
    for j in words[i]:
        if d.get(j) is None:
            result += 1
            break


print((len(words) - 1) - result)

    


# 10
# ABABA
# BBAAC
# BBAAD
# BBAAE
# BBAAB
# ACQAC
# LKJDS
# OKWLN
# OKNLS
# PONLM

# 10
# AAAB
# ABBA
# ABBB
# AAABC
# AAABB
# AABBB
# PABB
# ABCD
# AB
# ABA

# 2
# ABBBB
# A