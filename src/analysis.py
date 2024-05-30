from sklearn.linear_model import LinearRegression
import pandas as pd
import os

def analysis(file_name):
    df = pd.read_csv(file_name)

    df['t_2'] = df['t'] ** 2

    df.rename(columns={'t': 't_1', 'y': 'target'}, inplace=True)

    X = df[['t_2', 't_1']]
    y = df['target']

    model = LinearRegression()
    model.fit(X, y)

    loss = ((model.predict(X) - y) ** 2).sum()

    # print(f"{file_name} & {model.coef_[0]:.2f} & {model.coef_[1]:.2f} & {model.intercept_:.2f} & {loss:.8f} \\\\")

    df = pd.read_csv(file_name)

    df.rename(columns={'x': 'target'}, inplace=True)

    X = df[['t']]
    y = df['target']

    model = LinearRegression()
    model.fit(X, y)

    loss = ((model.predict(X.values) - y) ** 2).sum()

    print(f"{file_name} & {model.coef_[0]:.2f} & {model.intercept_:.2f} & {loss:.8f} \\\\")



for file in os.listdir('data'):
    if file.endswith('.csv'):
        analysis(f'data/{file}')
