# http://boj.kr/1259

# 1. 문자열길이/2 만큼을 돌면서 첫번째과 마지막인 같은지 확인

while True:
    isPalindrome = True
    s = input()
    if s == "0":
        break
    
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            isPalindrome = False
            break
        
    if isPalindrome:
        print("yes")
    else:
        print("no")
