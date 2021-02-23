# 문제를 잘 읽자.. 알겠어도 두 번 읽자..

# 1. bombs 앞문자가 아니라 끝 문자가 들어왔을 때 비교해야함
# 2. 파이썬 인덱스 개꿀

strings = list(input())
bombs = input()
tmp = []

for s in strings:
    tmp.append(s)
    if ''.join(tmp[-len(bombs):]) == bombs:
        del(tmp[-len(bombs):])


# while True:
#     if i >= len(strs) or len(strs) <= 0:
#         break
#     if strs[i] == bombs[0]:
#         tmp = ''.join(strs[i:i+len(bombs)])
#         if tmp == bombs:
#             del(strs[i:i+len(bombs)])
#             i -= 2
#     i += 1


if len(tmp) == 0:
    print("FRULA")
else:
    print(''.join(tmp))

# 테스트케이스
# aaababccbcbc
# abc