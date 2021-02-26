import sys
input = sys.stdin.readline

while 1:
    data = int(input())
    if data == 0:
        break
    str_data = '1' + str(data)
    chk = True
    size = (len(str_data) - 1)//2
    for i in range(1, size+1):
        if chk == False:
            break
        if str_data[i] != str_data[-i]:
            chk = False
    if chk:
        print("yes")
    else:
        print("no")
