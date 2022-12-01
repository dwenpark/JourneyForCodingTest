# 예제 4-3 왕실의 나이트

minx, miny = 1, 1
maxx, maxy = 8, 8

coordinate = input("where? ")

row = int(coordinate[1])
column = ord(coordinate[0])-ord("a") + 1

steps = [(-2,-1) , (-2, 1), (-1, -2), (1, -2), (2, 1), (2,-1), (1, 2), (-1, 2)]

result = 0
for step in steps:
	next_row = row + step[0]
	next_column = column + step[1]
	if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
		result += 1

print(result)
