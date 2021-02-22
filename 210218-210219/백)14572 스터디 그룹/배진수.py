import sys
input = sys.stdin.readline

n, k, d = map(int, input().split())
number = []
level = []
for i in range(n):
    algo, lev = map(int, input().split())
    level.append((lev, i))
    num = list(map(int, input().split()))
    number.append(num)
# level = [(20, 0), (10, 1), (0, 2)] => (실력, 해당학생의 순서)
# number = [[1], [2], [3]] => 학생 순서대로 알고있는 알고리즘

level.sort(reverse=True)
answer = 0
# for i in range(n-1):
#     cnt = 1
#     all_problem = set(number[level[i][1]])
#     all_can = number[level[i][1]]
#     for j in range(i+1, n):
#         if level[i][0] - level[j][0] <= d:
#             cnt += 1
#             all_can = list(set(all_can) & set(number[level[j][1]]))
#             all_problem.update(number[level[j][1]])
#             answer = max(answer, (len(all_problem) - len(all_can)) * cnt)
#             # print(all_problem, all_can, answer)
#         else:
#             break

for start in range(n):
    all_problem = set(number[level[start][1]])
    all_can = number[level[start][1]]
    end = start + 1
    cnt = 1
    while end < n:
        if level[start][0] - level[end][0] <= d:
            cnt += 1
            all_can = list(set(all_can) & set(number[level[end][1]]))
            all_problem.update(number[level[end][1]])
            answer = max(answer, (len(all_problem) - len(all_can)) * cnt)
            end += 1
            # print(all_problem, all_can, answer)
        else:
            break

print(answer)

"""
{1, 2} [] 4
{2, 3} [] 4
4
"""
