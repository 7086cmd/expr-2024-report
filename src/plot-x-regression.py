import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate some data
np.random.seed(0)
# 1000 random numbers from a normal distribution in [0, 10]
X = np.random.normal(0, 10, 1000)

df = pd.read_csv('data/2024-05-17(16-57-14).csv')

X = np.sort(X)

# \dfrac{1}{2} 4.88 * x ^ 2 + 0.08 * x - 0.00

y = 4.88 * X ** 2 + 0.08 * X - 0.00

# Plot the data

plt.plot(X, y, label='Predicted data')
plt.scatter(df['t'], df['y'], label='Generated data')
plt.title('Plot of the data')
plt.xlabel('time')
plt.ylabel('x-axis')
plt.xlim(0, 0.2)
plt.ylim(0, 0.2)
plt.legend()
plt.savefig('figures/plot-x-regression.eps')
