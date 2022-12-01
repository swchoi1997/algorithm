n = int(input())
for _ in range(n):
    sound = list(input().split())

    animal = []
    result = []
    while True:
        ani_sound = input()      
        if ani_sound == 'what does the fox say?':
            break
        new_ani_sound = ani_sound.split()
        animal.append(new_ani_sound[2])


    for i in sound:
        if i not in animal:
            result.append(i)


    for i in result:
        print(i, end = ' ')


