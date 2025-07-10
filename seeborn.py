import numpy as np
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dm_office_sales.csv")
print(tabulate(df.head(),headers="keys",tablefmt="simple"))
sns.scatterplot(x="salary",y="sales",data=df,s=200,style='level of education',
                hue="level of education",palette="Dark2")
plt.title("Salary Vs Sales")
# plt.show()
sns.displot(data=df,x="salary",bins=100,rug=True,kde=True)
plt.show()
