# http://boj.kr/1865

# 벨만포드 알고리즘 ...


def bf(start):
    for i in range(1, n+1):
        for j in range(1, n+1):
            for now, cost in graph[j]:
                
                if distance[now] > distance[j] + cost:
                    distance[now] = distance[j] + cost
                    if i == n:
                        return True
    return False
    
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)

    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        graph[e].append((s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))

    possible = bf(i)

    if possible:
        print("YES")
    else:
        print("NO")


