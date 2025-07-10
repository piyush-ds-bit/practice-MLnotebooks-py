

import numpy as np
import pandas as pd
import os
print(np.random.seed(101))
data=np.random.randint(0,101,(3,4))     #np.random.randint(start,end but not upto,size(row,column))
print(data)
my_index=["A","B","C"]
my_columns=["UT1","UT2","UT3","UT4"]
New_data=pd.DataFrame(data,my_index,my_columns)

print(New_data)
print(type(New_data))
