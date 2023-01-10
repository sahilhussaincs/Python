from sqlite3 import DatabaseError
import pandas as pd
import numpy as np
dt1 = np.array([10,20,30])
dt2 = np.array([1,2,3])
dt3 = np.array([100,200,300])
dFrame5 = pd.DataFrame([dt1, dt2,
dt3], columns=[ 'A', 'B', 'C'])
print(dFrame5)