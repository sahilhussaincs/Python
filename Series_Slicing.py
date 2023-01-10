import pandas as pd
seriesCapCntry = pd.Series(['NewDelhi', 'WashingtonDC', 'London',
'Paris'], index=['India', 'USA', 'UK', 'France'])
seriesCapCntry[1:3]
print(seriesCapCntry)