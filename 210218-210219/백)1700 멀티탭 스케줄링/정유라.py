# http://boj.kr/1700
n, m = map(int, input().split())

plugs = list(input().split())
tab = [0] * n
print(plugs)
new_plugs = ''.join(plugs)
cnt = 0
tab_idx = 0

# tab에 먼저 채워주기
for i in range(n):
    tab[i] = plugs[i]

for i in range(n, m):
    print("i:", i, "tab:", tab, "plugs:", plugs)
    # 꽂혀 있는 경우 패스
    if plugs[i] in tab:
        continue
    
    # 자리가 다 차 있는 경우
    else:
        for z in range(i, i+n+1):
            
        max_idx = 0
        for j in tab: # tab 안에서
            # tab 안의 원소를 찾다
            idx = new_plugs.rfind(j) 
            if max_idx < idx:
                max_idx = idx
        print("max_idx", new_plugs[max_idx])
        tab[max_idx] = plugs[i]
        cnt += 1


print(cnt)