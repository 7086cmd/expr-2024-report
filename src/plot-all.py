import matplotlib.pyplot as plt
import pandas as pd
import os

for file in os.listdir('data'):
    if file.endswith('.csv'):
        df = pd.read_csv(f'data/{file}')
        plt.scatter(df['x'], df['y'], label=file)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.savefig('figures/plot-all.eps')
