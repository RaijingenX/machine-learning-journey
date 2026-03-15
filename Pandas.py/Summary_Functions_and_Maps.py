# Topic  : Summary Functions and Maps
# Source : Kaggle Learn Pandas
# Explanation : Learn how to use summary functions and maps in Pandas to analyze and manipulate data


import pandas as pd


review = pd.read_csv('catalog.csv')



# 1. Use the .mean() method to calculate the average price of the products in reviews, assigning the result to variable avg_price.
avg_price = review['Price'].mean()
#print(avg_price)








# 2. Use the .median() method to calculate the median price of the products in reviews, assigning the result to variable median_price.

median_price = review['Price'].median()
#print(median_price)







# 3. Use the .unique() method to find the unique values in the 'Rating' column of reviews, assigning the result to variable unique_categories.

unique_categories = review['Rating'].unique()
#print(unique_categories)






# 4. Use the .value_counts() method to count the number of occurrences of each unique value in the 'Rating' column of reviews, assigning the result to variable rating_counts.
rating_counts = review['Rating'].value_counts()
#print(rating_counts)






# 5. Create variable centered_price containing a version of the price column with the mean price subtracted.

centered_price = review['Price'] - review['Price'].mean()
#print(centered_price)






# 6. Create variable price_label containing a version of the price column with the value 'expensive' if the price is above 100, and 'cheap' otherwise.

price_label = review['Price'].apply(lambda x: 'expensive' if x > 100 else 'cheap')
#print(price_label)






# 7. Make a function which returns 'good' if a rating is above 4, 'ok-ok' for ratings between 3 and 4, and 'bad' otherwise. Then, use the .apply() method to apply this function to the 'Rating' column of reviews, assigning the result to variable rating_label.
def label_rating(rating):
    if rating > 4:
        return 'good'
    elif rating >= 3:
        return 'ok-ok'
    else:
        return 'bad'

rating_label = review['Rating'].apply(label_rating)
#print(rating_label)