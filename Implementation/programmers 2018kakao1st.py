# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    tmp1 = []
    tmp2 = []
    for i,j in zip(arr1, arr2):
        tmp1.append(format(i,'b').zfill(n))
        tmp2.append(format(j,'b').zfill(n))

    answer = []
    for x in range(0, len(arr1)):
        tmp = ""
        for y in range(0, n):
            if tmp1[x][y] == "1" or tmp2[x][y] == "1":
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)
    return answer
