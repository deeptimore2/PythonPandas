import pandas as pd
import numpy as np

print(np.__version__)
print(pd.__version__)


#---numpy array
arr=np.arange(10)
series2= pd.Series(arr)
print("panda series:\n",series2)

series2[0]=100
print(series2)

#-----pandas series
series1=pd.Series([1,2,3,4,5])
series3=pd.Series([87,76,67,77],index=['A','B','C','D'])
print(series1)
print(type(series1))
print(series1[1:3])

print(series2.iloc[1:4])

print(series3.index)
print(series3.loc['B':'D'])
