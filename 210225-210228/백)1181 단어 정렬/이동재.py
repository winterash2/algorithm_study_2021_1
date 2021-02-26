import sys
N = int(input())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().rstrip())
words = list(words)
words.sort(key=lambda x: [len(x), x])
for word in words:
    print(word)


"""
import sys

N = int(input())
words = [[] for _ in range(51)]
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    words[len(word)].append(word)

for i in range(1, 51):
    # print(words[i])
    words[i] = list(set(words[i]))
    words[i].sort()
    for word in words[i]:
        print(word)
"""
