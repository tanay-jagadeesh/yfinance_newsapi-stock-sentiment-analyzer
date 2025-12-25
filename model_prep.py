import pandas as pd

df = pd.read_csv('features_scaled.csv')
print(df.columns)

#defined target variable
df['target'] = df['next_day_change']

#creating feature matrix X
#starting by dropping columns that are not needed for the prediction

matrix_x = df.drop(columns = ['ticker', 'date', 'date_dt', 'target', 'next_day_change'])

matrix_y = df['target']