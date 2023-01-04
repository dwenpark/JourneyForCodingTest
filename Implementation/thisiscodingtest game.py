# 예제 4-3 게임개발

map_size = list(input("map_size? "))
player = list(input("player? "))
direction = input("direction? ")

map = []
for i in range(int(map_size[0])):
	map.append(list(input(f"map_line {i} : ")))

been = []
been.append(player)
done = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


global x, y
x = int(player[0])
y = int(player[1])

def move(direction):
  	x += dx[direction]
  	y += dy[direction]
