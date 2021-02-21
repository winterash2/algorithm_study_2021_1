import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
students = []
for _ in range(N):
    numAlgo, power = map(int, input().split())
    algoList = list(map(int, input().split()))
    students.append((power, numAlgo, algoList))

students.sort()
# print(students)

dpAlgo = [0 for _ in range(K+1)]

# dpAlgo, knowAlgoNum, allAlgoNum 세 변수를 0번 학생이 있다고 가정하고 초기화함
power, numAlgo, algoList = students[0]
for algoNum in algoList:
    dpAlgo[algoNum] += 1

idxMin = idxMax = 0
result = 0
for i in range(1, N):
    idxMax = i
    # 가장 power가 적은 학생과의 실력차이가 D 이하가 될때까지 idxMin을 증가
    while students[idxMax][0] - students[idxMin][0] > D:
        power, numAlgo, algoList = students[idxMin]
        # idxMin에 해당하는 학생을 그룹에서 추방할 때 dpAlgo에 idxMin 학생이 알고있던 문제에 해당하는 값들을 1씩 뺌
        for algoNum in algoList:
            dpAlgo[algoNum] -= 1
        idxMin += 1

    # 새로 추가되는 idxMax 학생의 알고리즘 문제 
    power, numAlgo, algoList = students[idxMax]
    for algoNum in algoList:
        dpAlgo[algoNum] += 1 # 새로 추가되는 학생이 알고있는 문제 +1
    
    knowAlgoNum = 0
    allAlgoNum = 0
    for elem in dpAlgo:
        if elem == 0: # 아무도 모르면
            continue
        elif elem == (idxMax - idxMin + 1): # 전부 알고 있으면
            knowAlgoNum += 1
            allAlgoNum += 1
        else: # 한 명 이상 알고 있으면
            allAlgoNum += 1

    result = max(result, (allAlgoNum - knowAlgoNum) * (idxMax - idxMin + 1) )

# print(dpResult)
print(result)


"""
import sys
input = sys.stdin.readline

N, K, D = map(int, input().split())
students = []
for _ in range(N):
    numAlgo, power = map(int, input().split())
    algoList = list(map(int, input().split()))
    students.append([power, numAlgo, algoList])

students.sort()
# print(students)

dpAlgo = [0 for _ in range(K+1)]
knowAlgoNum = 0
allAlgoNum = 0

# dpAlgo, knowAlgoNum, allAlgoNum 세 변수를 0번 학생이 있다고 가정하고 초기화함
power, numAlgo, algoList = students[0]
for algoNum in algoList:
    dpAlgo[algoNum] += 1
    knowAlgoNum += 1
    allAlgoNum += 1

idxMin = idxMax = 0
dpResult = [0]
for i in range(1, N):
    idxMax = i
    # 가장 power가 적은 학생과의 실력차이가 D 이하가 될때까지 idxMin을 증가
    while students[idxMax][0] - students[idxMin][0] > D:
        power, numAlgo, algoList = students[idxMin]
        # idxMin에 해당하는 학생을 그룹에서 추방할 때 dpAlgo에 idxMin 학생이 알고있던 문제에 해당하는 값들을 1씩 뺌
        # 빼고 난 결과가 다 남은 사람들이 다 알고 있는 경우가 아니면 전부 알고 있는 알고리즘 문제 개수 -1
        # 모든 알고리즘의 수는 무조건 -1
        for algoNum in algoList:
            dpAlgo[algoNum] -= 1
            if dpAlgo[algoNum] == 0:
                allAlgoNum -= 1
        idxMin += 1

    knowAlgoNum = 0
    allAlgoNum = 0
    # 새로 추가되는 idxMax 학생의 알고리즘 문제 
    power, numAlgo, algoList = students[idxMax]
    for algoNum in algoList:
        dpAlgo[algoNum] += 1
        if dpAlgo[algoNum] == (idxMax - idxMin + 1):
            knowAlgoNum += 1
        if dpAlgo[algoNum] == 1:
            allAlgoNum += 1
    
    
    dpResult.append((allAlgoNum - knowAlgoNum) * (idxMax - idxMin + 1))

# print(dpResult)
print(max(dpResult))
"""