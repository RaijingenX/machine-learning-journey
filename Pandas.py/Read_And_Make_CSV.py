# Topic       : Pandas - Read and Make CSV file
# Source      : Kaggle Learn Pandas
# Explanation : Create a DataFrame named Data and make a CSV file named "Cricket.csv" from it.And learn to work with the Index column in the CSV file. 





import pandas as pd

Data = pd.DataFrame([["Rahul",1,67.90],["Rohit",2,78.90],["Virat",3,89.90],["Shikhar",4,90.90],["Surya",5,95.90]],columns = ["Name","Rank","Score"])

Data.to_csv("Cricket.csv",index = False)        #to save the DataFrame as a CSV file named "Cricket.csv" without including the index.

Data1 = pd.read_csv("Cricket.csv")              #to read the CSV file "Cricket.csv" and store it in a new DataFrame called Data1. The read_csv() function is used to read the CSV file and create a DataFrame from it.


print("DataFrame without using index_col")
print(Data1)

print()

Data2 = pd.read_csv("Cricket.csv",index_col = "Name")     #to read the CSV file "Cricket.csv" and set the "Name" column as the index of the DataFrame. The index_col parameter is used to specify which column should be used as the index.
print("DataFrame with 'Name' as index")
print(Data2)