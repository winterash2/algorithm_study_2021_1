n = int(input())    
coins = list(map(int, input().split()))
coins.sort()
price = 1
for coin in coins:
    if price < coin:
        break
    price += coin
    
    
    
print(price)