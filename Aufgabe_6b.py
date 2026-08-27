def compute_amount_with_minimal_coins_dp(coins: list[int], target_amount: int):
    
    # Erstellung einese Arrays zur Speicherung der Anzahl 
    # an benötigten Münzen für den jeweiligen Teilbetrag 
    memory = [float('inf')] * (target_amount + 1)
    # Ein Betrag 0 benötigt 0 Münzen => erstes Element = 0
    memory[0] = 0
   
    for coin in coins:
       for sub_amount in range(coin, target_amount + 1):
            # memory[i] enthält die minimale Anzahl an Münzen,
            # die benötigt werden, um den Betrag i zu bilden.
            
            # Für den aktuellen Teilbetrag werden zwei Möglichkeiten verglichen:
            # 1. Die bisher bekannte beste Lösung memory[sub_amount]
            # 2. Die Lösung für (sub_amount - coin) unter Verwendung der aktuellen Münze (+1)
            # Beispiel: sub_amount=3, coins=[3] => min(memory[3], memory[0] + 1) = min(3, 1) = 1  
            memory[sub_amount] = min(memory[sub_amount], memory[sub_amount - coin] + 1)
           
    # Ist der Wert des letzten Elements noch "Infinity", 
    # kann der Zielbetrag nicht aus den übergebenen Münzen gebildet werden
    if memory[target_amount] == float('inf'):
        return None
    
    return memory
                       
target_amount = 6
coins = [1, 3, 4]

result = compute_amount_with_minimal_coins_dp(coins, target_amount)
    
for i in range(1, target_amount+1):
    print(f'Needed {result[i]} coins for sub amount {i}')