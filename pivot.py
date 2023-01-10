import pandas as pd
data={'Store':['S1','S2','S3','S1','S2','S3','S1','S2','S3'], 'Year':[2016,2016,2016,2017,2017,2017,2018,2018,2018],'Total_sales(Rs)':[12000,330000,420000,
20000,10000,450000,30000, 11000,89000],'Total_profit(Rs)':[1100,5500,21000,32000,9000,45000,3000,
1900,23000]
}

df=pd.DataFrame(data)
S1df = df[df.Store=='S1']
S1df['Total_sales(Rs)'].sum()
62000
print(S1df)