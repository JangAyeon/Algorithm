import sys

input = sys.stdin.readline

def can_make(sign: str, name: str) -> bool:
    m, L = len(sign), len(name)
    if L > m:
        return False
    for start in range(m):
        if sign[start] != name[0]:
            continue
        if L == 1:
            return True
        max_d = (m - 1 - start) // (L - 1)
        for d in range(1, max_d + 1):
            ok = True
            for j in range(1, L):
                if sign[start + j * d] != name[j]:
                    ok = False
                    break
            if ok:
                return True
    return False

def main():
    N = int(input().strip())
    name = input().strip()
    count = 0
    for _ in range(N):
        sign = input().strip()
        if can_make(sign, name):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
