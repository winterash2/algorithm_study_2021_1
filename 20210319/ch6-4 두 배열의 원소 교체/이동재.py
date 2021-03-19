N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
A = A + B[:K]
A.sort(reverse=True)
answer = 0
for i in range(N):
    answer += A[i]
print(answer)
"""
5 3
1 2 5 4 3
5 5 6 6 5
"""