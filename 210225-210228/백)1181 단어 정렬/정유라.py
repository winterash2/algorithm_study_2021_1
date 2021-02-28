# http://boj.kr/1181

n = int(input())
s = set()
for _ in range(n):
    s.add(input().rstrip())

answer = sorted(s, key=lambda x: [len(x),x])

for word in answer:
    print(word)


# arr = []
# for _ in range(int(input())):
#     s = input()
#     arr.append((len(s), s))

# arr.sort()
# for i in range(len(arr)):
#     if i == 0:
#         tmp = "0"
#     else:
#         tmp = arr[i-1]
#     if arr[i] == tmp:
#         continue
#     print(arr[i][1])