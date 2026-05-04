# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Start coding here! Use as many cells as you like
netflix_movies = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies_1990 = netflix_movies[netflix_movies["release_year"] >= 1990]
netflix_movies_1999 = netflix_movies_1990[netflix_movies_1990["release_year"] <= 1999]

plt.hist(netflix_movies_1999["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

action_movies = netflix_movies_1999[netflix_movies_1999["genre"] == "Action"]

short_movie_count = 0

for label, row in action_movies.iterrows():
    if row["duration"] < 90:
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)
