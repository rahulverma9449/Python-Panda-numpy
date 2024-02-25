# Function Definition
def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    return result if amount == 0 else []

# Example Input
coins_input = [25, 10, 5, 1]
amount_input = 63

# Function Call
result_output = greedy_coin_change(coins_input, amount_input)

# Output
print(f"Input Coins: {coins_input}")
print(f"Amount: {amount_input}")
print(f"Result: {result_output}")
