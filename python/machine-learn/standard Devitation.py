import math

data = [12, 18, 14, 20, 16]

mean = sum(data) / len(data)
var = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(var)
print(f"Standard Deviation: {std_dev}")