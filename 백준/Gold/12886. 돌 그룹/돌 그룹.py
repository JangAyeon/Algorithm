from collections import deque

def can_make_equal(A, B, C):
    total = A + B + C
    
    # 총 돌 개수가 3으로 나누어 떨어지지 않으면 절대 같아질 수 없음
    if total % 3 != 0:
        return 0
    
    # BFS를 위한 큐
    queue = deque()
    queue.append((A, B, C))
    
    # 방문한 상태 저장 (set을 사용)
    visited = set()
    visited.add((A, B, C))

    # BFS 실행
    while queue:
        x, y, z = queue.popleft()
        
        # 세 그룹이 모두 같아지면 1 반환
        if x == y == z:
            return 1
        
        # 두 개의 그룹을 선택하여 돌 개수 변경
        for a, b in [(x, y), (y, z), (x, z)]:
            if a != b:
                # 항상 작은 값이 a, 큰 값이 b가 되도록 정렬
                a, b = min(a, b), max(a, b)
                
                # 새로운 상태 계산
                new_a = a + a
                new_b = b - a
                new_c = total - (new_a + new_b)  # 남은 한 그룹 계산
                
                # 정렬하여 방문 체크 (순서 상관없이 같은 상태로 인식)
                new_state = tuple(sorted((new_a, new_b, new_c)))
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

    return 0  # 모든 경우를 다 탐색했는데 같아질 수 없다면 0

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(can_make_equal(A, B, C))
