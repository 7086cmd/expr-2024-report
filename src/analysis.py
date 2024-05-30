from sklearn.linear_model import LinearRegression
import pandas as pd
import os

def analysis(file_name):
    df = pd.read_csv(file_name)

    df['t_2'] = df['t'] ** 2

    df.rename(columns={'t': 't_1', 'y': 'target'}, inplace=True)

    X = df[['t_1', 't_2']]
    y = df['target']

    model = LinearRegression()
    model.fit(X, y)

    coef = model.coef_

    v0 = coef[0]
    a = coef[1] * 2

    print([a, v0, model.intercept_])

for file in os.listdir('data'):
    if file.endswith('.csv'):
        analysis(f'data/{file}')
