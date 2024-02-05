# -*- coding: utf-8 -*-
"""

@author: nkheswa
"""

import pandas as pd

#---------------------------------------------------------------------

''' Question 1
'''
df = pd.read_csv('movie_dataset.csv')
highest_rated_movie = df[df['Rating'] == df['Rating'].max()]['Title'].values[0]
print('\nQ1')
print(highest_rated_movie)

'''Answer:
    The Dark Knight
'''
#---------------------------------------------------------------------

''' Question 2
'''
average_revenue = df['Revenue (Millions)'].mean()
print('\nQ2')
print(average_revenue)

'''Answer:
    82.95637614678898 (Million)
'''
#---------------------------------------------------------------------

''' Question 3
'''
# Filter the dataframe for movies released between 2015 and 2017
filtered_df = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_2017 = filtered_df['Revenue (Millions)'].mean()
print('\nQ3')
print(average_revenue_2015_2017)

'''Answer:
    63.099905660377345 (Million)
'''
#---------------------------------------------------------------------

''' Question 4
'''

# Filter the dataframe for movies released in 2016
movies_2016 = df[df['Year'] == 2016]

# Count the number of movies released in 2016
num_movies_2016 = len(movies_2016)

print('\nQ4')
print(num_movies_2016)

'''Answer:
    297
'''
#---------------------------------------------------------------------

''' Question 5
'''
# To find the number of movies directed by Christopher Nolan
num_movies_nolan_directed = df[df['Director'] == 'Christopher Nolan'].shape[0]

print('\nQ5')
print(num_movies_nolan_directed)

'''Answer:
    5
'''
#---------------------------------------------------------------------

''' Question 6
'''
# Count the number of movies with a rating of at least 8.0
num_high_rated_movies = df[df['Rating'] >= 8.0].shape[0]
print('\nQ6')
print(num_high_rated_movies)

'''Answer:
    78
'''
#---------------------------------------------------------------------

''' Question 7
'''

# Filter the dataframe for movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_nolan_directed = nolan_movies['Rating'].median()
print('\nQ7')
print(median_rating_nolan_directed)

'''Answer:
    8.6
'''
#---------------------------------------------------------------------

''' Question 8
'''

# Calculate the average rating for each year and find the year with the highest average rating
yearly_average_rating = df.groupby('Year')['Rating'].mean()
year_with_highest_rating = yearly_average_rating.idxmax()

print('\nQ8')
print(year_with_highest_rating)

'''Answer:
    2007
'''
#---------------------------------------------------------------------

''' Question 9
'''

# Count the number of movies made in 2006
num_movies_2006 = df[df['Year'] == 2006].shape[0]

# Count the number of movies made in 2016
num_movies_2016 = df[df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print('\nQ9')
print(percentage_increase)

'''Answer:
    575.0 (%)
'''
#---------------------------------------------------------------------

''' Question 10
'''
from collections import Counter

# Combine all the actor names into a single list
all_actors = df['Actors'].str.split(', ').sum()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0]

print('\nQ10')
print(most_common_actor)

'''Answer:
    ('Mark Wahlberg', 15)
'''
#---------------------------------------------------------------------

''' Question 11
'''

# Split the genres and create a list of all unique genres
unique_genres = set(df['Genre'].str.split(',').explode())

# Count the number of unique genres
num_unique_genres = len(unique_genres)

print('\nQ11')
print(num_unique_genres)

'''Answer:
    20
'''
#---------------------------------------------------------------------

