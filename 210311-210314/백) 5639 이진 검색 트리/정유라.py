# http://boj.kr/5639

import sys
input = sys.stdin.readline

data = []
while True:
    try:
        data.append(int(input()))
    except:
        break

def post_order(root, node):
    if root < node:
    
