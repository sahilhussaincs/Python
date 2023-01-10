import pandas as pd


df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23],
                   'assists': [5, 7, 7, 9, 12, 9],
                   'rebounds': [11, 8, 10, 6, 6, 5]})

#view DataFrame
print(df)
df.to_csv(r'F:\Python\mydata.csv',index=False)