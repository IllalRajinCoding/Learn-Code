import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

sns.scatterplot(x="sepal_length", y="sepal_width", data=df, hue="species")
plt.title('Scatter Plot: Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()