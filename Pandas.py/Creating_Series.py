# Topic   : Pandas - Creating Series
# Source  : Kaggle Learn Pandas
# Explanation : Creating a Series named "Dinner" with data stored in list (quantities,items) and print it. 


import pandas as pd

quantities = ["4 cups","1 cup","2 large","1 can"]
items = ["Flour","Milk","Eggs","Spam"]
ingredients = pd.Series(quantities,index = items,name = "Dinner")
print(ingredients)