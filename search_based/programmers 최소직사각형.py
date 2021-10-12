# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max1 = 0
    max2 = 0
    for size in sizes:
        size.sort()
        if size[0] > max1:
            max1 = size[0]
        if size[1] > max2:
            max2 = size[1]
    return max1 * max2