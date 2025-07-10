import pandas as pd
from tabulate import tabulate
training=pd.read_csv("aug_train.csv")
print('*'*200)
print(tabulate(training.head(),headers='keys',tablefmt='simple'))
# print()
print('*'*200)
print()
zomato=pd.read_csv('zomato.csv',encoding='latin-1')
# print(tabulate(zomato.head(),headers='keys',tablefmt='simple'))
# new_data=zomato.groupby(["Restaurant Name","Country Code"]).mean()
# print(tabulate(new_data,headers='keys',tablefmt='simple'))
