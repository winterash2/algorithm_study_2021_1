# 고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미한다. 
# 모든 원소가 오름차순으로 정렬된 수열에 고정점이 있다면 고정점을 출력하는 프로그램을 작성하시오. 
# 단, O(logN)에 해결하시오.

def find_pin(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        
        # 고정점이 존재하면 고정점이 위치하는 왼쪽의 모든 원소들은 (인덱스 > 원소값)이 되고
        elif mid > array[mid]:
            start = mid + 1
        
        # 고정점 오른쪽의 모든 원소들은 (인덱스 < 원소값)이 된다 
        else:
            end = mid - 1
    return -1

n = int(input())
array = list(map(int, input().split()))

print(find_pin(array, 0, n-1))