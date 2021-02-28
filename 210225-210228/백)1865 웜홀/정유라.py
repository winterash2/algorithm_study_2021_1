# http://boj.kr/1865

# 벨만포드 알고리즘
# 음수간선이 있는 경우 + 음수 간선 순환이 있는경우

# 1. 출발노드설정
# 2. 최단거리 테이블 초기화
# 3. 다음의 과정을 N-1 번 반복
#   1) 전체 간선 E개를 하나씩 확인
#   2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산 -> 최단거리 테이블 갱신
# * 만약 음수간선 사이클 발생하는지 체크-> 3번 과정을 한번 더 수행, 이때 최단거리 테이블이 갱신된다면 음수간선사이클 존재.


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


