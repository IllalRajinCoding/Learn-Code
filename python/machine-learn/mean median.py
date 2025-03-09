import pandas

data = [12, 18, 20, 14, 16]

mean = sum(data) / len(data)
print(f"mean: {mean}")


sorted_data = sorted(data)
n = len(sorted_data)
median = (sorted_data[n // 2] + sorted_data[(n - 1) // 2]) / 2
print(f"median: {median}")

from statistics import mode

mode_value = mode(data)
print(f"mode: {mode_value}")