testcase = int(input())

x_mining = [-1, 0, 1]
y_mining = [1, 1, 1]

def mining(res, times, n, m, x, y):
    global gold_mine, result
    print(x,y,times,res)
    if times == m:
        result = max(res, result)
        # print(res)
    
    else:
        for i in range(3):
            dx = x + x_mining[i]
            dy = y + y_mining[i]
            if 0 <= dx < n  and 0 <= dy < m:
                res += gold_mine[dx][dy]
                times += 1
                mining(res, times, n, m, dx, dy)
                times -= 1
                res -= gold_mine[dx][dy]

for _ in range(testcase):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    gold_mine = []
    for i in range(1,n+1):
        gold_mine.append(list(data[((i-1)*m):(i*m)]))
    
    result = -1e9
    times = 1
    for i in range(n):
        mining(gold_mine[i][0], times, n, m, i, 0)
        print(result)

    print(result)
