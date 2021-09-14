import pandas as pd

#iphone_df = pd.read_csv('data/iphone.csv')
#iphone_df = pd.read_csv('data/iphone.csv', header= None)
iphone_df = pd.read_csv('data/iphone.csv', index_col=0)
#index0 부분을 row로 설정

print(iphone_df)