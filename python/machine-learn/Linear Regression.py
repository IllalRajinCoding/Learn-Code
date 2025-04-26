from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

plt.scatter(x, y, alpha=0.5, label = "Original Data")
plt.plot(x_test, y_pred, color='red', label = "Predicted Data")
plt.title('Linear Regression: Predicted vs Original Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")