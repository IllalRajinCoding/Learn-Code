from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = 2 * np.random.rand(100, 1) - 3
y = 0.5 * x**2 + x + 2 + np.random.randn(100, 1)

poly_features = PolynomialFeatures(degree=2, include_bias=False)
x_poly = poly_features.fit_transform(x)

poly_reg = LinearRegression()
poly_reg.fit(x_poly, y)

x_new = np.linspace(-3, 3, 100).reshape(100, 1)
x_new_poly = poly_features.transform(x_new)
y_new = poly_reg.predict(x_new_poly)


plt.scatter(x, y, alpha=0.5, label="Original Data")

plt.show()