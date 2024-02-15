# 2018 KAKAO BLIND RECRUITMENT [1차] 캐시

from collections import deque 

def solution(cacheSize, cities):
    l = [""]*cacheSize
    cache = deque(l, maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer+=1
        else:
            cache.append(city)
            answer+=5
    print(cache)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))