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

# 재귀함수로
"""
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