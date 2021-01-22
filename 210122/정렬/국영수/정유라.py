# https://www.acmicpc.net/problem/10825

n = int(input())
student_score = []
"""
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuck 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taehwan 50 60 90
"""

for _ in range(n):
    name, kor, eng, math = input().split()
    student_score.append((name, int(kor), int(eng), int(math)))

student_score.sort(key=lambda x: ( -int(x[1]), int(x[2]), -int(x[3]), x[0]))
print(student_score)
for student in student_score:
    print(student[0])