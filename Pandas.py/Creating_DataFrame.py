# Topic       : Pandas - Creating DataFrame
# Source      : Kaggle Learn Pandas
# Explanation : Create a DataFrame name fruits and print it. The DataFrame should have the following data: 
#               Apples  Bananas  Oranges 
#    2017 Sales  30       21        10
#    2018 Sales  24       67        45
#    2019 Sales  45       78        34
#    2020 Sales  12       54        56
# The columns should be named "Apples", "Bananas", and "Oranges". The index should be named "2017 Sales", "2018 Sales", "2019 Sales", and "2020 Sales". 


import pandas as pd

fruits = pd.DataFrame([[30,21,10],[24,67,45],[45,78,34],[12,54,56]],columns = ["Apples","Bananas","Oranges"],index = ["2017 Sales","2018 Sales","2019 Sales","2020 Sales"])
print(fruits)