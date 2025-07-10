

import numpy as np
import pandas as pd



help(pd.Series)
indexx=[2,1,0]
data=["Dirghayu","Ayushman","anantayu"]
myarray=pd.Series(data,indexx)
print(myarray)
# print(type(myarray))
print(myarray[2])
print(myarray[0])

ratio={"English":25,"Maths":20,"Science":23}

print(type(ratio))
print(pd.Series(ratio))

series_1={"Japan":80,"Bharat":100,"China":50,"Nepal":76}
series_2={"Brazil":90,"Bharat":90,"China":89,"Nepal":95}
series_3=pd.Series(series_1)
series_4=pd.Series(series_2)
print(series_3)
print(series_4)

# Now do remember that,if we multiply a list or string it will be like this
# [1,2] * 3 = [1,2,1,2,1,2]
# but in numpy,it will multiply with the elements inside it....See the Environment file in this

new_series=series_3.add(series_4,fill_value=0)
print(new_series)
