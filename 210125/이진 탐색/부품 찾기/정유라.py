def check_item(array, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    if array[mid] == target:
        return True

    if array[mid] > target:
        return check_item(array, target, start, mid - 1)
    else:
        return check_item(array, target, mid + 1, end)
    

n = int(input())
my_item = list(map(int, input().split()))
my_item.sort() # 님아 그 sort를 잊지마오..

m = int(input())
customer_want = list(map(int, input().split()))

for i in customer_want:
    if check_item(my_item, i, 0, n - 1) == True:
        print("yes")
    else:
        print("no")
