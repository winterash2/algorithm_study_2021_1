n = int(input())

student_info = []
for i in range(n):
    name, score = input().split()
    student_info.append((name, int(score)))

def setting(data):
    return data[1]

result = sorted(student_info, key=setting)

for name, score in result:
    print(name, end=" ")
