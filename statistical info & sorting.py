import numpy as np
import pandas as pd
from tabulate import tabulate

from DataFrame2 import sales_data

print(tabulate(sales_data.describe(),headers='keys',tablefmt='simple'))
print(tabulate(sales_data.describe().transpose(),headers='keys',tablefmt='simple'))
