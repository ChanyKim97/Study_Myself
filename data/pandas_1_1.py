import pandas as pd

df = pd.read_csv('data/mega_millions.csv', index_col=0)

print(df)