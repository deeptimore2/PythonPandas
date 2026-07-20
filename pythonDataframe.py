import pandas as pd

#empty data frame
df=pd.DataFrame()
print(df)

#--creates a new column
df["SQL"]=[78,89,55]
df["PYTHON"]=[88,90,93]

df.loc[len(df)]=[97,84]
print(df)

#-------------------------------

data = { 
        'apples sales': [3,2,0,1,9,6,3,2,7], 
        'oranges sales': [0,3,7,2,2,5,8,7,1]   
    }
#idx = ['2000', '2001', '2002', '2003', '2004','2005', '2006', '2007', '2008']
idx=pd.RangeIndex(2000,2009)
fruitsdf=pd.DataFrame(data,index=idx)
print(fruitsdf)
print(fruitsdf.shape)
print(fruitsdf.dtypes)
print(fruitsdf.index)
print(fruitsdf.index[0])
print(fruitsdf.index[-1])
print(fruitsdf.index.tolist())

#----------------------------------------------
#--read from csv file
print("============Read from CSV")
employee_df=pd.read_csv('files/employee.csv')
print(employee_df)
print(employee_df.info())
print(employee_df.describe())
print(employee_df.head())
print(employee_df.tail())

#------------Read fron json file--------------
print("============Read from JSON")
cardf=pd.read_json('files/cars.json')
print(cardf)
print(cardf.info())
print(cardf.describe())
print(cardf.describe(include='all'))
#--------------------------------------------
#-------------Column attributes-------------

# Create DataFrame from a dictionary
student_dict = {    
    'Name': ['Joe', 'Nat', 'Harry'],  
    'Age': [20, 21, 19],  
    'Marks': [85.10, 77.80, 91.54]
    }
student_df = pd.DataFrame(student_dict)

# Get the column names as a Pandas Index object
columns_index = student_df.columns
print("Columns (Index):", columns_index)

# Get the label of the first column
first_column = student_df.columns[0]
print("First Column Name:", first_column)

# Get the column names as a list
columns_list = student_df.columns.tolist()
print("Columns (List):", columns_list)

#select the single column
print(student_df['Name'][0])
print(student_df['Age'][2])

#select multiple columns
print(student_df[['Name', 'Age']])
print(student_df.columns[2])
print(student_df[['Marks']])

print(student_df['Marks'].value_counts())
print("----")
print(student_df['Marks'].value_counts().sort_index(ascending=True))
#---------------------------------------------------------------------

technologies = (
    {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas","Oracle","Java"],
    'Fee' :[20000,25000,26000,22000,24000,21000,22000],
    'Duration':['30day', '40days' ,'35days', '40days', '60days', '50days', '55days']
    }
    )
df = pd.DataFrame(technologies)
print(df.columns)

# Rename a Single Column 
df2=df.rename(columns = {'Courses':'Courses_Name','Duration':'Course_Duration'}) # rename the column from Courses to Courses_Name.
print(df2.columns)
print(df.insert(3,'Enrolled',value=True))
print("----------------------")
asdf=df.assign(Enrolled=False)
print("-----------------------")
print(asdf.head())