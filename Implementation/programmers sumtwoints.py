# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i:
                answer.append(numbers[j] + numbers[i])
    return sorted(list(set(answer)))