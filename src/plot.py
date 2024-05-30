import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/2024-05-17(16-57-14).csv')

plt.scatter(df['x'], df['y'], label='tag')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Trace of the tag')
plt.legend()
plt.savefig('figures/plot1.eps')
