import copy
def solution(name):
    moves = [-1, 1]
    nameList = list(name)
    # start = (nameList, index, count)
    def bfs(start):
        stack = [start]
        
        while stack:
            array, idx, cnt = stack.pop()
            cnt += min(ord(array[idx]) - 65, 91 - ord(array[idx]))
            array[idx] = 'A'
            if array.count('A') == len(array): 
                return cnt
            for move in moves:
                new_array = copy.deepcopy(array) 
                new_idx = idx + move
                new_cnt = cnt + 1
                stack.insert(0, (new_array, new_idx, new_cnt))

    return bfs((nameList, 0, 0))