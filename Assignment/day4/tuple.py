# Given tuple of tuples
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))


result = []

# Number of columns
cols = len(data[0])

for i in range(cols):
    total = 0
    for row in data:
        total += row[i]
    result.append(total / len(data))

print(result)
