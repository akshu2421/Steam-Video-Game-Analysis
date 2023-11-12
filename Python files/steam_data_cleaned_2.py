#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:44:06 2023

@author: akshatathopte
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


# Load the dataset into a pandas DataFrame
df = pd.read_csv('/Users/akshatathopte/Documents/Steam Video games Analysis/Dataset/steam.csv')


# Clean the "steamspy_tags" column
df['steamspy_tags'] = df['steamspy_tags'].apply(lambda x: x.split(';')[0])


# Split the 'genres' column into binary values

df['action'] = df['genres'].apply(lambda x: 1 if 'Action' in x.split(';') else 0)
df['free_to_play'] = df['genres'].apply(lambda x: 1 if 'Free to Play' in x.split(';') else 0)
df['Strategy'] = df['genres'].apply(lambda x: 1 if 'Strategy' in x.split(';') else 0)
df['Adventure'] = df['genres'].apply(lambda x: 1 if 'Adventure' in x.split(';') else 0)
df['Indie'] = df['genres'].apply(lambda x: 1 if 'Indie' in x.split(';') else 0)
df['Animation & Modeling'] = df['genres'].apply(lambda x: 1 if 'Animation & Modeling' in x.split(';') else 0)
df['Casual'] = df['genres'].apply(lambda x: 1 if 'Casual' in x.split(';') else 0)
df['Simulation'] = df['genres'].apply(lambda x: 1 if 'Simulation' in x.split(';') else 0)
df['Racing'] = df['genres'].apply(lambda x: 1 if 'Racing' in x.split(';') else 0)
df['Massively Multiplayer'] = df['genres'].apply(lambda x: 1 if 'Massively Multiplayer' in x.split(';') else 0)
df['Nudity'] = df['genres'].apply(lambda x: 1 if 'Nudity' in x.split(';') else 0)
df['Violent'] = df['genres'].apply(lambda x: 1 if 'Violent' in x.split(';') else 0)
df['RPG'] = df['genres'].apply(lambda x: 1 if 'RPG' in x.split(';') else 0)
df['Sports'] = df['genres'].apply(lambda x: 1 if 'Sports' in x.split(';') else 0)
df['Gore'] = df['genres'].apply(lambda x: 1 if 'Gore' in x.split(';') else 0)
df['Early Access'] = df['genres'].apply(lambda x: 1 if 'Early Access' in x.split(';') else 0)
df['Utilities'] = df['genres'].apply(lambda x: 1 if 'Utilities' in x.split(';') else 0)
df['Video Production'] = df['genres'].apply(lambda x: 1 if 'Video Production' in x.split(';') else 0)
df['Design & Illustration'] = df['genres'].apply(lambda x: 1 if 'Design & Illustration' in x.split(';') else 0)
df['Software Training'] = df['genres'].apply(lambda x: 1 if 'Software Training' in x.split(';') else 0)
df['Web Publishing'] = df['genres'].apply(lambda x: 1 if 'Web Publishing' in x.split(';') else 0)
df['Education'] = df['genres'].apply(lambda x: 1 if 'Education' in x.split(';') else 0)
df['Audio Production'] = df['genres'].apply(lambda x: 1 if 'Audio Production' in x.split(';') else 0)
df['Sexual content'] = df['genres'].apply(lambda x: 1 if 'Sexual content' in x.split(';') else 0)
df['Game development'] = df['genres'].apply(lambda x: 1 if 'Game development' in x.split(';') else 0)

# Drop the original "steamspy_tags" column
df.drop('genres', axis=1, inplace=True)


# Split the 'categories' column into binary values

df['Full Controller Support'] = df['categories'].apply(lambda x: 1 if 'Full Controller Support' in x.split(';') else 0)
df['Steam Cloud'] = df['categories'].apply(lambda x: 1 if 'Steam Cloud' in x.split(';') else 0)
df['Steam Trading Cards'] = df['categories'].apply(lambda x: 1 if 'Steam Trading Cards' in x.split(';') else 0)
df['Co-op'] = df['categories'].apply(lambda x: 1 if 'Co-op' in x.split(';') else 0)
df['Local Co-op'] = df['categories'].apply(lambda x: 1 if 'Local Co-op' in x.split(';') else 0)
df['Online Co-op'] = df['categories'].apply(lambda x: 1 if 'Online Co-op' in x.split(';') else 0)
df['Shared/Split Screen'] = df['categories'].apply(lambda x: 1 if 'hared/Split Screen' in x.split(';') else 0)
df['Cross-Platform Multiplayer'] = df['categories'].apply(lambda x: 1 if 'Cross-Platform Multiplayer' in x.split(';') else 0)
df['Steam Achievements'] = df['categories'].apply(lambda x: 1 if 'Steam Achievements' in x.split(';') else 0)
df['Includes level editor'] = df['categories'].apply(lambda x: 1 if 'Includes level editor' in x.split(';') else 0)
df['Steam Workshop'] = df['categories'].apply(lambda x: 1 if 'Steam Workshop' in x.split(';') else 0)
df['In App Purchase'] = df['categories'].apply(lambda x: 1 if 'In App Purchase' in x.split(';') else 0)
df['Partial Controller Support'] = df['categories'].apply(lambda x: 1 if 'Partial Controller Support' in x.split(';') else 0)
df['Full controller support'] = df['categories'].apply(lambda x: 1 if 'Full controller support' in x.split(';') else 0)
df['VR Support'] = df['categories'].apply(lambda x: 1 if 'VR Support' in x.split(';') else 0)
df['Includes Source SDK'] = df['categories'].apply(lambda x: 1 if 'Includes Source SDK' in x.split(';') else 0)
df['Anti-Cheat enabled'] = df['categories'].apply(lambda x: 1 if 'Anti-Cheat enabled' in x.split(';') else 0)
df['Multi-player'] = df['categories'].apply(lambda x: 1 if 'Multi-player' in x.split(';') else 0)
df['Local Multi-player'] = df['categories'].apply(lambda x: 1 if 'Local Multi-player' in x.split(';') else 0)
df['Single-player'] = df['categories'].apply(lambda x: 1 if 'Single-player' in x.split(';') else 0)
df['MMO'] = df['categories'].apply(lambda x: 1 if 'MMO' in x.split(';') else 0)
df['Captions available'] = df['categories'].apply(lambda x: 1 if 'Caption available' in x.split(';') else 0)


# Drop the original "steamspy_tags" column
df.drop('categories', axis=1, inplace=True)


# Split the platforms column into separate strings
platforms = df['platforms'].str.split(';')

# Create new columns for each platform
df['Linux'] = platforms.apply(lambda x: 1 if 'linux' in x else 0)
df['Windows'] = platforms.apply(lambda x: 1 if 'windows' in x else 0)
df['Mac'] = platforms.apply(lambda x: 1 if 'mac' in x else 0)

# Drop the original platforms column
df.drop('platforms', axis=1, inplace=True)

# Print the resulting dataframe
print(df.head())

# Converting the owners columns to a specific number
def range_to_avg(range_val):
    range_vals = range_val.split('-')
    return str((int(range_vals[0]) + int(range_vals[1])) / 2)
df['owners'] = df['owners'].apply(range_to_avg)
df['owners'] = pd.to_numeric(df['owners'], errors='coerce')

# Split the release date into separate columns
df['day'] = pd.to_datetime(df['release_date']).dt.day
df['month'] = pd.to_datetime(df['release_date']).dt.month
df['year'] = pd.to_datetime(df['release_date']).dt.year

# Drop the original release_date column
df.drop('release_date', axis=1, inplace=True)

# Print the resulting dataframe
print(df.head())


df.to_csv("steam_log.csv", index=False)


