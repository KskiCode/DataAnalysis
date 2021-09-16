import pandas as pd
import matplotlib.pyplot as plt

movies = pd.read_csv('./data/NetflixOriginals.csv', encoding="ISO-8859-1")
movies.head()

movies.info() # no null-values

# Top 20 movies(title) by rating? / Worst 20 movies(title) by rating?
top_movies = movies.nlargest(10, 'IMDB Score', keep='all') # do not drop any duplicates, even it means selecting more than n items.
top_movies[['Title','IMDB Score']]

bad_movies = movies.nsmallest(10, 'IMDB Score', keep='all')
bad_movies[['Title', 'IMDB Score']]

# Which genre has the biggest share?
movies.Genre.value_counts()
movie_genre_share = movies.Genre.value_counts(normalize=True)*100 # get share of genres 


genre_share_10 = movie_genre_share.nlargest(10) # 10 largest shares of genre - first: documentary with 27.23%, second: Drama with 13.18%  
genre_share_10.index
genre_share_10.plot(kind='bar', xlabel='Genre (Top 10 Genre by share)', ylabel='Number of Movies from Genre', figsize=(8, 4), grid=True)
plt.show()

# Average runtime of movies in each genre? 
genre_runtime = movies.groupby(['Genre']).mean()
genre_runtime_20 = genre_runtime['Runtime'].nlargest(20, keep='all')
genre_runtime_20.plot(kind='bar', xlabel='Genre', ylabel='Avg. Runtime in minutes', figsize=(8, 4)) # x-axis name not displayed?
plt.show()

# Is there a correlation between runtime and IMDB Score
print(movies.corr())
movies.plot(kind='scatter', x='IMDB Score', y='Runtime', color='red')
plt.show()

# create new column for premiere with to_datetime()
movies['PremiereDate'] = pd.to_datetime(movies['Premiere'])
movies['year'] = movies['PremiereDate'].dt.year
movies['month'] = movies['PremiereDate'].dt.month

movies.month.value_counts().plot(kind='bar', xlabel='month', ylabel='No. of movies premiered', 
                                title='No of movies released by month', grid=True)
plt.show()