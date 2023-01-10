import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mela.csv")
df.plot(kind='line', color=['red','blue','green'],marker="*",markersize=10,linewidth=3,linestyle="--")
# Set title to "Mela Sales Report"
plt.title('Sales Report')
# Label x axis as "Days"
plt.xlabel('Days')
# Label y axis as "Sales in Rs"
plt.ylabel('Sales in Rs')
#Display the figure
plt.show()