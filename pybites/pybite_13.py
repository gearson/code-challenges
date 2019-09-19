#%% 
from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve, urlopen
import pandas as pd

#%%
movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'days/04-06-collections/movies.csv'
urlretrieve(movie_data, movies_csv)
#%%
df_movies = pd.read_csv(movies_csv)
df_movies.head()
#%%
df_movies.director_name.value_counts()
#%%
directors = set(df_movies.director_name)
mean_scores = [df_movies[df_movies['director_name'] == director]['imdb_score'].mean() for director in directors]
#%%
mean_scores[:5]

#%%
with open(movies_csv, encoding='utf-8') as csvfile:
    test = csvfile.readlines()

#%%
Movie = namedtuple('Movie', 'title year score')
# this is kinda like Movie is the class with title,year and score methods

#%%
def get_movies_by_director(data=movies_csv):

    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']  # get values from the OrderedDict
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            m = Movie(title=movie, year=year, score=score)  # Movie is a namedtuple
            #print(m.title)
            directors[director].append(m)

    return directors

#%%
directors = get_movies_by_director()
directors['George Lucas']