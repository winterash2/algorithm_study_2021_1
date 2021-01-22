N = int(input())
houses = list(map(int, input().split()))
houses.sort()

print(houses[ (N-1) // 2])

# 시간 초과
"""
import math
max_distance = max(houses)

distances = []
for i in range(max_distance):
    distances.append( (sum([abs(x-i) for x in houses]), i) )

distances.sort()
print(distances[0][1])
"""
