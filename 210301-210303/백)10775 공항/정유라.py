# http://boj.kr/10775
import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parnet = [0] * (g+1)
for i in range(1, g+1):
    parnet[i] = i

def find(parent, x):
    if parnet[x] != x:
        parnet[x] = find(parnet, parnet[x])
    return parnet[x]

def union(parent, a, b):
    a = find(parnet, a)
    b = find(parnet, b)

    if a < b:
        parnet[b] = a
    else:
        parnet[a] = b


result = 0
for i in range(p):
    plane = int(input())
    plane_root = find(parnet, plane)
    if plane_root == 0:
        break
    union(parnet, plane_root, plane_root-1)
    result += 1

print(result)