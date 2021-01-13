# n = int(input())
# course = input().split()
n = 5
course = ['R', 'R', 'R', 'U', 'D', 'D']

point = dict()
point['x'] = 1
point['y'] = 1

for c in course:
    if c == 'L':
        if point['x'] > 1:
            point['x'] -= 1
    if c == 'R':
        if point['x'] < n:
            point['x'] += 1
    if c == 'U':
        if point['y'] > 1:
            point['y'] -= 1
    if c == 'D':
        if point['y'] < n:
            point['y'] += 1
    
print(point['y'], point['x'])