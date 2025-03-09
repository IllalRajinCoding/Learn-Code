import matplotlib.pyplot as plt
import numpy as np

exam_score = np.random.normal(0, 1, 100)

plt.hist(exam_score, bins=30, edgecolor='black')
plt.title('Normal Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
