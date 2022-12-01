start_B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

start_W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

a, b = map(int, input().split())
maps = []
for _ in range(a):
    bnw = input()
    maps.append(list(bnw))

result = 64
# print(maps)
for i in range(a - 8 + 1):
    for j in range(b - 8 + 1):        
        count_B = 0
        count_W = 0
        for x in range(8):
            for y in range(8):
                if maps[i + x][j + y] != start_B[x][y]:
                    count_B += 1

                elif maps[i + x][j + y] != start_W[x][y]:
                    count_W += 1

        result = min(result, count_W, count_B)
        

print(result)


                
                        

