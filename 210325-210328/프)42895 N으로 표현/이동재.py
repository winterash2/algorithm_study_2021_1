


def dfs(result, count, Ns, number):
    if result == number:
        return count
    if count >= 8:
        return 1e9
    answer = 1e9
    for i in range(len(Ns)):
        answer = min(answer, dfs(result+Ns[i], count + i + 1, Ns, number))
    for i in range(len(Ns)):
        answer = min(answer, dfs(result-Ns[i], count + i + 1, Ns, number))
    for i in range(len(Ns)):
        answer = min(answer, dfs(result*Ns[i], count + i + 1, Ns, number))
    for i in range(len(Ns)):
        answer = min(answer, dfs(result//Ns[i], count + i + 1, Ns, number))
    return answer
    
    


def solution(N, number):
    Ns = []
    num = ''
    for _ in range(8):
        num = int(str(num) + str(N))
        Ns.append(num)
    
    answer = dfs(0, 0, Ns, number)
    if answer > 8:
        answer = -1
    return answer


print(solution(5, 12))
