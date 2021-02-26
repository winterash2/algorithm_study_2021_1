while True:
    word = input()
    if word == '0':
        break
    word = list(word)
    isPalindrome = True
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            isPalindrome = False
            break
    if isPalindrome:
        print('yes')
    else:
        print('no')