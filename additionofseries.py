import pandas as pd
import numpy as np
seriesA = pd.Series([1,2,3,4,5], index =
['a', 'b', 'c', 'd', 'e'])
seriesB = pd.Series([10,20,-10,-50,100],
index = ['z', 'y', 'a', 'c', 'e'])
totalseries= (seriesA+ seriesB)
print(totalseries)