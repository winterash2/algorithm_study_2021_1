def solution(n, weak, dist):
    answer = 1
    data = []
    for w in weak:
        if w < weak[0] + int(n/2):
            data.append(w - weak[0])
        else:
            data.append(-(w - weak[0]))
    data = data.sort()

    if data[-1] - data[0] in dist:
        return  1
    
    for i in range(1, len(data)):
        a = data[-1] - data[i]
        b = data[i-1] - data[0]

    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]