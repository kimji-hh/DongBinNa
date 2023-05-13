# 왕실의 나이트

coor = input()
row = int(coor[1])
column = int(ord(coor[0])) - int(ord('a')) + 1 # a의 아스키코드값 97을 빼서 1을 의미
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (-1, -2),(1, -2), (1, 2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
