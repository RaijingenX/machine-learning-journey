# Topic  : Pandas - Indexing, Selection, and Assigning
# Source : Kaggle Learn Pandas
# Explanation : Learn how to select and assign values in a DataFrame using various indexing techniques. This includes selecting specific columns, rows, and applying conditions to filter data.


import pandas as pd

catalog = pd.DataFrame({'Product ' : ['Table', 'Chair', 'Sofa', 'Bed','Lamp', 'Bookshelf', 'Desk', 'Dresser', 'Nightstand', 'Wardrobe'],
                        'Price' : [200, 100, 500, 800, 50, 150, 300, 400, 250, 600],
                        'Stock' : [10, 20, 5, 2, 50, 15, 8, 3, 12, 4],
                        'Rating' : [4.5, 4.0, 4.8, 4.2, 3.9, 4.3, 4.6, 4.1, 4.0, 4.7],
                        'Warranty' : [2, 1, 3, 5, 1, 2, 4, 3, 2, 5],
                        'Service' : ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes']},index = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'])

catalog.to_csv('catalog.csv', index = True)        #to save the DataFrame as a CSV file named "catalog.csv" including the index.

review = pd.read_csv('catalog.csv')




# 1.  Select the Product column from reviews and assign the result to the variable prod

prod = review['Product ']
#print(prod)

# NOTE : -  we can choose review.Product  instead of review['Product '] to select the Product column from reviews and assign the result to the variable prod. This is a more concise way to access the column, but it only works if the column name does not contain spaces or special characters.







# 2. Select the first value from the Product column of reviews, assigning it to variable first_product
first_product = review['Product '].iloc[0]
#print(first_product)

# NOTE : -  while this is the preferred way to obtain the entry in the DataFrame, many other options will return a valid result, such as reviews.Product.loc[0], reviews.Product[0], and more!







# 3. Select the first row of data (the first record) from reviews, assigning it to the variable first_row.

first_row = review.iloc[0]
#print(first_row)







#4. Select the first 10 values from the Product column in reviews, assigning the result to variable first_Products.

first_Products = review['Product '].iloc[:10]
#print(first_Products)

# NOTE : - Many other options will return a valid result, such as prod.head(10) and reviews.loc[:9, "Product "].






#5. Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.

sample_reviews = review.loc[[1, 2, 3, 5, 8]]
#print(sample_reviews)







#6. Create a variable df containing the Product, Price,and Warranty columns of the records with the index labels 0, 1, 5, and 9.

df = review.loc[[0, 1, 5, 9], ['Product ', 'Price', 'Warranty']]
#print(df)






#7. Create a variable df containing the Product and Rating columns of the first 5 records.

df = review.loc[:4, ['Product ', 'Rating']]
#print(df)






#8. Create a DataFrame Ratings containing reviews of Product whose Rating is greater than 4.5 .

Ratings = review[review['Rating'] > 4.5]
#print(Ratings)

# NOTE : -  we can also use review.loc[review['Rating'] > 4.5] to create the DataFrame Ratings containing reviews of Product whose Rating is greater than 4.5. This is another way to filter the DataFrame based on a condition.






# 9. Create a DataFrame Goods containing reviews of Product whose Service is "Yes" and warranty is greater than 4 .

Goods = review[(review['Service'].isin(['Yes'])) & (review['Warranty'] > 4)]

#print(Goods)

# NOTE : -  we can also use review.loc[(review['Service'] == 'Yes') & (review['Warranty'] > 4)] to create the DataFrame Goods containing reviews of Product whose Service is "Yes" and warranty is greater than 4. This is another way to filter the DataFrame based on multiple conditions.




# 10. Create a DataFrame Cheap containing reviews of Product whose Price is less than 300 and Stock is greater than 5.

Cheap = review[(review['Price'] < 300) & (review['Stock'] > 5)]
#print(Cheap)