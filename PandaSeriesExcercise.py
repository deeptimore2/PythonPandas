import pandas as pd
import numpy as np

print("------------Panda Series Excercises------------")
#--------------------Problem  1-----------------------------------
#  Convert the 3 objects below into 3 seperate Pandas Series objects.
#  Use the .head() method to see the first 5 items in each Series


mylist = list('abcedfghijklmnopqrstuvwxyz') # Converts the string of letters into a list of individual characters.
myarr = np.arange(26) # Creates a NumPy array of numbers from 0 to 25.
mydict = dict(zip(mylist, myarr)) # Combines the list and array into key-value pairs to create a dictionary mapping each letter to a number.

print("List:", mylist)
print("Array:", myarr)
print("Dictionary:", mydict)

serList = pd.Series(data=mylist,name='alphabet') # problem 2 ,3 implemented --added name as parameter
serArr = pd.Series(data=myarr,name='alphabet1') #problem 2, 3 implemented --added name as parameter
serDic = pd.Series(data=mydict,name='alphabet2') #problem 2 ,3 implemented --added name as parameter

print("---------------List to Series-------------\n",serList.head())
print("---------------Array to Series------------\n",serArr.head())
print("---------------dictionary to Series-----------------\n",serDic.head())


#--------------------------------------------------
#------------Problem 4-----------------------------
#--------------------------------------------------

ser1= pd.Series([2, 4, 6, 8, 10])
ser2= pd.Series([1, 3, 5, 7, 9])

serAdd = pd.Series(ser1 + ser2) # alternative method ser1.add(ser2)
serSub =pd.Series(ser1 - ser2) #
ser1.sub(ser2)
serMul=pd.Series(ser1 * ser2)
serDiv = pd.Series(ser1 / ser2)

print("Addition of two series :",serAdd)
print("SUbtraction between two series :",ser1.sub(ser2))
# print("Multiplication between two series :",serMul)
# print("Division between two series :",serDiv)

#--------------------------------------------------
#------------Problem 5-----------------------------
#--------------------------------------------------