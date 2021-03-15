import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def post(start, end):
    if start > end:
        return
    else:
        root = pre[start]
        div = end + 1
        for pos in range(start+1, end+1):
            if root < pre[pos]:
                div = pos
                break
        post(start+1, div-1)
        post(div, end)
        print(root)


pre = []
while True:
    try:
        x = int(input())
        pre.append(x)
    except:
        break
post(0, len(pre)-1)
            
