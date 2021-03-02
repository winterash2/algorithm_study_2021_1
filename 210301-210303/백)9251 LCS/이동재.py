str1 = list(input())
str2 = list(input())
graph = [[0 for _ in range(len(str1))] for _ in range(len(str2))]


# 배열 맨 위쪽이랑 맨 왼쪽 초기화
maxVal = 0
for i in range(len(str2)):
    if str2[i] == str1[0]:
        graph[i][0] = 1
        maxVal = 1
    else:
        graph[i][0] = maxVal
maxVal = 0
for j in range(len(str1)):
    if str1[j] == str2[0]:
        graph[0][j] = 1
        maxVal = 1
    else:
        graph[0][j] = maxVal


# 초기화 끝내고 이제 도는 시간
for i in range(1, len(str2)):
    for j in range(1, len(str1)):
        if str1[j] == str2[i]:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j], graph[i-1][j-1] + 1)
        else:
            graph[i][j] = max(graph[i][j-1], graph[i-1][j])

print(graph[len(str2)-1][len(str1)-1])
