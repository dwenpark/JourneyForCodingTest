# 예제 4-1 상하좌우

N = int(input("정사각형 공간의 한 변의 크기? (int) :"))
route = input("이동할 계획서 내용? (리스트) : ")

coordinate = [1, 1]

for i in route:
	if i == "R" and coordinate[1] < N:
		coordinate[1] += 1
	elif i == "L" and coordinate[1] > 1:
		coordinate[1] -= 1
	elif i == "U" and coordinate[0] > 1:
		coordinate[0] -= 1
	elif i == "D" and coordinate[0] < N:
		coordinate[0] += 1

print(coordinate)