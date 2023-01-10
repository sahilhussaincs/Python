from venv import create
import pandas as pd
import pymysql as py
import sqlalchemy 
engine=create('mysql+pymysql://root:smsmb@localhost:3306/CARSHOWROOM')
data={'ShowRoomId':[1,2,3,4,5],'Location':['Delhi','Bangalore','Mumbai','Chandigarh','Kerala']}
df=pd.DataFrame(data)
df.to_sql('showroom_info',engine,if_exists="replace",index=False)