# http://boj.kr/1865

# 벨만포드 알고리즘 ...


def bf(start):
    for i in range(1, n+1):
        for j in range(1, n+1):
            for end, cost in graph[j]:
                print("-----end:", end, ", j:", j, ", i:",i)

                if distance[end] > distance[j] + cost:
                    print(distance)
                    distance[end] = distance[j] + cost
                    print(distance)
                    if i == n:
                        print("n:", n)
                        print(distance)
                        return True
    return False
    
for _ in range(int(input())):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [int(1e9)] * (n+1)
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


