import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate some data
np.random.seed(0)
# 1000 random numbers from a normal distribution in [0, 10]
X = np.random.normal(0, 1, 1000)

df = pd.read_csv('data/2024-05-17(16-57-14).csv')

X = np.sort(X)

# 1.75 * x + 0.06

y = 1.75 * X + 0.06

# Plot the data

plt.plot(X, y, label='Predicted data')
plt.scatter(df['t'], df['x'], label='Generated data')
plt.title('Plot of the data')
plt.xlabel('time')
plt.ylabel('y-axis')
plt.xlim(0, 0.2)
plt.ylim(0, 0.4)
plt.legend()
plt.savefig('figures/plot-y-regression.eps')
