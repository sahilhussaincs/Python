import pandas as pd
import matplotlib.pyplot as plt
data ={'Name':['Ravi','Sonu','Monu','Tonu'],
    'Hieght':[10,20,30,40],
    'Weight':[11,22,33,44]
}
df=pd.DataFrame(data)
df.plot(kind='hist',edgecolor='Green',linewidth=2,linestyle=':',fill=False,hatch='o')
plt.show()