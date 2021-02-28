# http://boj.kr/1018

# 국밥코드 참고함
n, m = map(int, input().split())
chess = []
for i in range(n):
    chess.append(list(input()))

chess_start_W = ['WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW']
chess_start_B = ['BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB']

def find(x, y):
    cnt_W = 0
    cnt_B = 0
    for i in range(8):
        for j in range(8):
            if chess_start_W[i][j] != chess[x+i][y+j]:
                cnt_W += 1
            if chess_start_B[i][j] != chess[x+i][y+j]:
                cnt_B += 1
    return min(cnt_W, cnt_B)

answer = 1e9
for i in range(0, n-7):
    for j in range(0, m-7):
        answer = min(answer, find(i, j))
print(answer)




# 나는 밥오..

# 1. 8x8이 움직일 수 있는 범위
# 2. 다시 칠해야하는 칸 체크
#    1) WBWBWBWB, BWBWBWBW 이랑 비교
#    2) 다르면 range(8)돌면서 다른 부분 count + 1
# 1의 범위에서 count가 작으면 갱신

# def find(s, WB):
#     # print("in find WB:", WB)
#     if s == WB:
#         return 0
#     s_l = list(s)
#     WB_l = list(WB)
#     cnt = 0
#     for i in range(8):
#         if s_l[i] != WB_l[i]:
#             cnt += 1
#     return cnt

# n, m = map(int, input().split())
# chess = []
# for i in range(n):
#     chess.append(list(input()))
# W = 'WBWBWBWB'
# B = 'BWBWBWBW'
# isWB = False # W
# answer = 1e9

# for i in range(0, n-7):
#     for j in range(0, m-7):
#         total = 0

#         # 범위 안의 체스
#         for k in range(i, i+8):
#             s = ''.join(chess[k][j:j+8])
            
#             if k == i:
#                 find_with_W = find(s, W)
#                 find_with_B = find(s, B)
#                 if find_with_W <= find_with_B:
#                     total += find_with_W
#                     continue
#                 else:
#                     total += find_with_B
#                     continue

#             if isWB:
#                 WB = W
#             else:
#                 WB = B

#             total += find(s, WB)
#             isWB = not isWB

#         if answer > total:
#             answer = total
# print(answer)