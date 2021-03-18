def jump(stones, k, mid):
    jump_count = k
    for stone in stones:
        if stone <= mid:
            jump_count -= 1
            if jump_count == 0:
                return False
        else:
            jump_count = k
    return True

def solution(stones, k):
    niniz = 0
    left = 0
    right = 200000000
    
    while left <= right:
        # 니니즈 친구들의 수
        mid = (left + right) // 2
        
        if jump(stones, k, mid):
            niniz = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return niniz + 1