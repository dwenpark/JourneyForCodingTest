# https://programmers.co.kr/learn/courses/30/lessons/49994#

def solution(dirs):
    lst = []
    right = 0
    up = 0
    next_right = 0
    next_up = 0
    for i in dirs:
        right = next_right
        up = next_up
        if i == "L" and right != -5:
            next_right -= 1
        elif i == "R" and right != 5:
            next_right += 1
        elif i == "U" and up != 5:
            next_up += 1
        elif i == "D" and up != -5:
            next_up -= 1
        else:
            continue
        lst.append(str(right)+str(up)+str(next_right)+str(next_up))
        lst.append(str(next_right)+str(next_up)+str(right)+str(up))
    return len(list(set(lst)))/2