def computeAmountWithMinimalCoins(coins: list[int], targetAmount: int):
    required_coins = {}
    coins = sorted(coins, reverse=True)
    
    for coin in coins:
        while coin <= targetAmount:
            required_coins[coin] = required_coins.get(coin, 0) + 1
            targetAmount -= coin
            
    return required_coins


coins = [50, 20, 10, 5, 2, 1]
print(computeAmountWithMinimalCoins(coins, 87))