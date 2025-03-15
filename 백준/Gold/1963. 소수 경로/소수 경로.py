from collections import deque
from itertools import permutations

# 에라토스테네스의 체로 4자리 소수를 미리 구함
def get_prime_numbers():
    primes = [True] * 10000
    primes[:2] = [False, False]  # 0과 1은 소수가 아님
    for i in range(2, 10000):
        if primes[i]:
            for j in range(i * i, 10000, i):
                primes[j] = False
    return {i for i in range(1000, 10000) if primes[i]}

prime_set = get_prime_numbers()

def bfs(start, target):
    if start == target:
        return 0
    
    queue = deque([(start, 0)])  # (현재 숫자, 변경 횟수)
    visited = set()
    visited.add(start)

    while queue:
        current, steps = queue.popleft()
        str_current = str(current)

        for i in range(4):  # 4자리 숫자의 각 자리 변경
            for digit in '0123456789':
                if str_current[i] == digit:
                    continue
                
                new_number = int(str_current[:i] + digit + str_current[i+1:])
                
                if new_number in prime_set and new_number not in visited:
                    if new_number == target:
                        return steps + 1
                    queue.append((new_number, steps + 1))
                    visited.add(new_number)

    return "Impossible"

# 입력 처리
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(bfs(a, b))
