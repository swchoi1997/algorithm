# 왕실의 나이트
n, m = input() # 나이트의 현재 위치 입력받기 둘 다 문자열로 입력받음

row = int(ord(n)) - int(ord('a')) + 1 #열, x 각 문자의 아스키 코드 값을 받아서 아스키 값의 최소인 a를 뺀 후 + 1 을 더하면 a = 1 b = 2 이렇게 값이 나오게 됨
column = int(m) # 행, y 둘다 문자열로 입력받았기 때문에 int로 형변환이 필요하다
count = 0
night_move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2),(-1, 2), (1, 2)] #나이트가 이동 할 수 있는 모든 방향을 나타냄

for i in range(len(night_move)):
    next_row = row + night_move[i][0]
    next_column = column + night_move[i][1]

    if next_row < 1 or next_row > 8 or next_column < 1 or next_column > 8:
        continue
    else:
        count += 1 # 나이트의 다음 값을 지정하는게 아니라 갈 수 잇는 장소의 갯수를 나타내면 되기때문에 count를 이용하였고 다음위치는 업데이트 하지 않았음

print(count)