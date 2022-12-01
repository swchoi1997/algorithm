Eng = input().upper()
new_Eng=list(set(Eng))

set_Eng = []
for i in new_Eng:
    set_ = Eng.count(i)
    set_Eng.append(set_)
print(new_Eng, set_Eng)
if set_Eng.count(max(set_Eng))>=2:
    print('?')
else:
    print(new_Eng[set_Eng.index(max(set_Eng))])

