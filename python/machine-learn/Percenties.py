import numpy as np
import matplotlib.pyplot as plt

data = [12, 18, 14, 20, 16, 70]
p_25 = np.percentile(data, 25)
p_50 = np.percentile(data, 50)
p_75 = np.percentile(data, 75)

print(f"25th Percentile: {p_25}")
print(f"50th Percentile: {p_50}")
print(f"75th Percentile: {p_75}")

plt.boxplot(data)
plt.title("Boxplot")
plt.xlabel("Data")
plt.ylabel("Value")
plt.show()