import numpy as np
import pandas as pd
from tabulate import tabulate
sales_data = pd.DataFrame({
    'Order ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Product': ['Laptop', 'Tablet', 'Laptop', 'Monitor', 'Printer',
                'Tablet', 'Laptop', 'Monitor', 'Printer', 'Tablet'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Office Supplies',
                 'Electronics', 'Electronics', 'Electronics', 'Office Supplies', 'Electronics'],
    'Region': ['North', 'South', 'East', 'West', 'North',
               'South', 'East', 'West', 'North', 'South'],
    'Quantity': [2, 5, 1, 4, 2, 3, 2, 1, 4, 5],
    'Price per Unit': [800, 300, 850, 200, 150, 310, 900, 210, 140, 320],
    'Sales Date': ['2024-01-15', '2024-02-18', '2024-03-10', '2024-01-22', '2024-02-12',
                   '2024-02-28', '2024-03-05', '2024-01-30', '2024-02-25', '2024-03-15']
})
# print(tabulate(sales_data,headers='keys',tablefmt='simple'))
# sales_data=sales_data.set_index('Sales Date')
# print(tabulate(sales_data,headers='keys',tablefmt='simple'))
# sales_data=sales_data.reset_index()
# print(tabulate(sales_data,headers='keys',tablefmt='simple'))

def profitable(Quantity,Price_per_unit):
    answer=Quantity*Price_per_unit
    if Quantity*Price_per_unit <1000:
        return "ok"
    elif (1000<Quantity*Price_per_unit<=1500):
        return "Thats awesome"
    else:
        return "Extraordinary"


def Amount(Quantity,Price_per_unit):
    answer=Quantity*Price_per_unit
    return answer

# sales_data["Sale"]=sales_data[["Quantity","Price per Unit"]].apply(lambda sales_data: profitable(sales_data["Quantity"],sales_data["Price per Unit"]),axis=1)
# OR WE CAN TRY THESE GIVEN METHOD
sales_data["Amount Received"]=np.vectorize(Amount)(sales_data["Quantity"],sales_data["Price per Unit"])
sales_data["Sale"]=np.vectorize(profitable)(sales_data["Quantity"],sales_data["Price per Unit"])
print(tabulate(sales_data,headers='keys',tablefmt='simple'))

print()
print()
print()

print(sales_data["Price per Unit"].max())
print(sales_data["Price per Unit"].idxmax())
print(sales_data["Price per Unit"].min())
print(sales_data["Price per Unit"].idxmin())
print(sales_data.iloc[2])

print()
print()
print()
print()

# for categorical columns
print(sales_data["Region"].value_counts())
print(sales_data["Region"].unique())
print(sales_data["Region"].nunique())
print(sales_data["Product"].value_counts())

print()
print()
print()

print(sales_data.map())
