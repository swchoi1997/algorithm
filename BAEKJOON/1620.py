import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

pocket = dict()

for i in range(n):
    name = str(input().rstrip())
    pocket[str(i + 1)] = name
    pocket[name] = str(i + 1)

# print(pocket)
for i in range(1, m + 1):
    ans = str(input().rstrip())

    print(pocket[ans])


# 26 5
# Bulbasaur
# Ivysaur
# Venusaur
# Charmander
# Charmeleon
# Charizard
# Squirtle
# Wartortle
# Blastoise
# Caterpie
# Metapod
# Butterfree
# Weedle
# Kakuna
# Beedrill
# Pidgey
# Pidgeotto
# Pidgeot
# Rattata
# Raticate
# Spearow
# Fearow
# Ekans
# Arbok
# Pikachu
# Raichu
# 25
# Raichu
# 3
# Pidgey
# Kakuna