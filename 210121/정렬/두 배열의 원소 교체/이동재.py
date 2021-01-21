N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        temp = A[i]
        A[i] = B[i]
        B[i] = temp
    else:
        break

print(sum(A))