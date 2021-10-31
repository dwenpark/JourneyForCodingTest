# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        if city.upper() not in cache:
            answer += 5
            cache.append(city.upper())
            if len(cache) > cacheSize:
                cache.popleft()
        else:
            cache.remove(city.upper())
            cache.append(city.upper())
            answer += 1
    return answer