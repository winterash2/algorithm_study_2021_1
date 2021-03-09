import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u) # 입력을 이쁘게 안 줄수도 있어서 양방향으로 넣어야 함

# dp[n][0] 은 자기가 포함 안 된 경우 dp[n][1] 은 자기가 포함 된 경우
dp = [[0, 0] for _ in range(N+1)]

q = [1]
for elem in q:
    visited[elem] = True
    for f in tree[elem]:
        if visited[f]:
            continue
        q.append(f)

q = q[::-1]
for id in q:
    dp[id][0] = 0
    dp[id][1] = 1
    for f in tree[id]:
        dp[id][0] += dp[f][1]
        dp[id][1] += min(dp[f][0], dp[f][1])

print(min(dp[1][0], dp[1][1]))

# def dfs(id):
#     dp[id][0] = 0
#     dp[id][1] = 1
#     for f in tree[id]:
#         if visited[id]: # 양방향으로 넣었기 때문에 역으로는 가면 안 되기 때문
#             continue
#         dfs(f)
#         dp[id][0] += dp[f][1]
#         dp[id][1] += min(dp[f][0], dp[f][1])

# dfs(1)
# print(min(dp[1][0], dp[1][1]))


# 이건 맞긴 한데 recursion error 뜸
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u) # 입력을 이쁘게 안 줄수도 있어서 양방향으로 넣어야 함

# dp[n][0] 은 자기가 포함 안 된 경우 dp[n][1] 은 자기가 포함 된 경우
dp = [[0, 0] for _ in range(N+1)]

def dfs(id):
    dp[id][0] = 0
    dp[id][1] = 1
    for f in tree[id]:
        if visited[id]: # 양방향으로 넣었기 때문에 역으로는 가면 안 되기 때문
            continue
        dfs(f)
        dp[id][0] += dp[f][1]
        dp[id][1] += min(dp[f][0], dp[f][1])

dfs(1)
print(min(dp[1][0], dp[1][1]))
"""

# 자식 노드에서 부모 노드로 타고 내려가면서 계산 - 실패
"""
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)


def solution(tree, id):  # [a = 자기가 포함된거, b = 자기가 안 포함된거]
    if tree[id] == []:
        return [1, 0]
    curA = 1
    curB = 0
    for f in tree[id]:
        a, b = solution(tree, f)
        curA += min(a, b)
        curB += min(a, b+1)
    return [curA, curB]

answer = solution(tree, 1)
print(min(answer))
"""

# 큐 이용 - 실패
"""
import sys
from collections import deque
input = sys.stdin.readline

class Node:
    def __init__(self, id):
        self.id = id
        self.friends = []

    def add_friend(self, friendID):
        self.friends.append(friendID)

    def get_friends(self):
        return self.friends

    def __str__(self):
        result = str(self.id) + ": "
        for f in self.friends:
            result += str(f)
            result += ' '
        return result

N = int(input())
node = [Node(i) for i in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    node[u].add_friend(v)

# [print(x) for x in node]

answer = [0, 0]
q = deque()
q.append(1)
depth = 0
while q:
    depth += 1
    for _ in range(len(q)):
        cur = q.popleft()
        # print(cur)
        answer[depth%2] += 1
        for f in node[cur].get_friends():
            q.append(f)

print(min(answer))
"""
# 재귀함수로 - 실패
"""
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, id):
        self.id = id
        self.friends = []

    def add_friend(self, friendID):
        self.friends.append(friendID)

    def get_friends(self):
        return self.friends

    def __str__(self):
        result = str(self.id) + ": "
        for f in self.friends:
            result += str(f)
            result += ' '
        return result

def solution(node, id, depth, answer):
    answer[depth % 2] += 1
    for f in node[id].get_friends():
        solution(node, f, depth+1, answer)

N = int(input())
node = [Node(i) for i in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    node[u].add_friend(v)

# [print(x) for x in node]

answer = [0, 0]
solution(node, 1, 0, answer)
print(min(answer))
"""

"""
14
1 2
1 3
1 4
2 5
2 6
4 7
4 8
7 9
9 10
9 11
9 12
9 13
9 14
"""