from math import gcd


def solution(w, h):
    answer = w * h
    gcdVal = gcd(w, h) # 겹치는게 있는 부분은 총 gcdVal개 있음
    w = w // gcdVal
    h = h // gcdVal

    b = max(w, h)
    s = min(w, h)
    trash = 0
    trash += (2 * (s-1))
    trash += (b - (s-1))
    trash *= gcdVal
    answer -= trash
    return answer


print(solution(8, 12))
