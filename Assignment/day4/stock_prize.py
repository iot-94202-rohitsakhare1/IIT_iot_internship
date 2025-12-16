prices = [105, 110, 108, 112, 115, 116, 114]

for i in range(len(prices) - 2):
    print(sub(prices[i:i+3]) / 3)
