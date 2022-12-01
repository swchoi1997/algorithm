n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))

# min_rgb = [0] * n
# min_rgb[0] = min(rgb[0])

# mem = rgb[0].index(min_rgb[0])

# for i in range(1, n):
#     print(mem)
#     if mem == 0:
#         min_rgb[i] = min(rgb[i][1], rgb[i][2])
#     elif mem == 1:
#         min_rgb[i] = min(rgb[i][0], rgb[i][2])
#     elif mem == 2:
#         min_rgb[i] = min(rgb[i][0], rgb[i][1])
    
#     mem = rgb[i].index(min_rgb[i])
# print(sum(min_rgb))

for i in range(1, n):
    rgb[i][0] = min(rgb[i -1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i -1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i -1][1], rgb[i-1][0]) + rgb[i][2]

print(min(rgb[n-1][0],rgb[n-1][1],rgb[n-1][2]))