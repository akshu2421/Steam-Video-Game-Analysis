# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 18:22:41 2023

@author: Riddhi Umap
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Load the Steam game data
steam_df = pd.read_csv("cleaned_steam_game_data.csv", usecols=["name", "action -G", "free_to_play - G", "Strategy - G", "Adventure - G", "Indie - G", "Animation & Modeling - G", "Casual - G", "Simulation - G", "Racing - G", "Massively Multiplayer - G", "Nudity - G", "Violent - G", "RPG - G", "Sports - G", "Gore - G", "Early Access -G", "Utilities-G", "Video Production -G", "Design & Illustration-G", "Software Training-G", "Web Publishing-G", "Education-G", "Audio Production-G", "Sexual content-G", "Game development-G","Full Controller Support-C", "Steam Cloud-C", "Steam Trading Cards -C", "Co-op-C", "Local Co-op -C", "Online Co-op-C", "Shared/Split Screen -C", "Cross-Platform Multiplayer -C", "Steam Achievements-C", "Includes level editor-C", "Steam Workshop-C", "In App Purchase-C", "Partial Controller Support-C", "Full controller support-C", "VR Support-C", "Includes Source SDK-C", "Anti-Cheat enabled-C", "Multi-player-C", "Local Multi-player-C", "Single-player-C", "MMO-C"])

# Apply the Apriori algorithm to identify frequent itemsets
frequent_itemsets = apriori(steam_df.drop("name", axis=1), min_support=0.05, use_colnames=True)

# Apply association rule mining to generate rules based on the frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Convert frozenset to string and remove "frozenset" and curly braces
rules["antecedents"] = rules["antecedents"].apply(lambda x: str(x).replace("frozenset({'", "").replace("'})", ""))
rules["consequents"] = rules["consequents"].apply(lambda x: str(x).replace("frozenset({'", "").replace("'})", ""))

# Export the association rule output to a CSV file
rules.to_csv("game_genre_rules.csv", index=False)

