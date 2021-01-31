import copy

def solution(words, queries):
    answer = []
    words_origin = copy.copy(words)
    max_len = max([len(x) for x in words])
    words = [ [] for _ in range(max_len+1)]

    for word in words_origin:
        words[len(word)].append(word)
    print(words)

    print(ord(' '))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]
print(solution(words, queries))