#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 16:43:02 2023

@author: linhnguyen
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

data = pd.read_csv('~/Downloads/cleaned_steam_game_data.csv')

X = data.drop(['name','release_date','developer','publisher','tag1', 'tag2', 'tag3','day'], axis=1)

scaler = StandardScaler()
X_std = scaler.fit_transform(X)

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))

distortions = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_std)
    distortions.append(kmeans.inertia_)
ax.plot(range(1, 11), distortions, marker='o', label='Distortion')
ax.set_xlabel('Number of clusters')

silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_std)
    score = silhouette_score(X_std, kmeans.labels_)
    silhouette_scores.append(score)
ax2 = ax.twinx()
ax2.plot(range(2, 11), silhouette_scores, marker='o', color='orange', label='Silhouette score')
ax2.set_ylabel('Silhouette score')

ax.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()

distortions = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_std)
    distortions.append(kmeans.inertia_)

plt.plot(range(1, 11), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

from sklearn.metrics import silhouette_score

silhouette_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X_std)
    score = silhouette_score(X_std, kmeans.labels_)
    silhouette_scores.append(score)

plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_std)

cluster_labels = kmeans.labels_

cluster_df = pd.DataFrame(X)
cluster_df['cluster'] = kmeans.labels_
cluster_summary = cluster_df.groupby('cluster').agg('mean')

# Add a column for the number of observations in each cluster
cluster_summary['count'] = cluster_df['cluster'].value_counts()

print(cluster_summary)

cluster_counts = cluster_summary['count']

plt.bar(cluster_counts.index, cluster_counts)

plt.xlabel('Cluster')
plt.ylabel('Number of observations')
plt.xticks(cluster_counts.index)
plt.show()

cluster_summary_T = cluster_summary.T

cluster_summary_T = cluster_summary_T.drop('count')

features_of_interest = ['owners']
cluster_summary_filtered = cluster_summary[features_of_interest]

cluster_summary_filtered_T = cluster_summary_filtered.T
cluster_summary_filtered_T = cluster_summary_filtered_T.rename_axis('')


cluster_summary_filtered_T.plot(kind='bar')

plt.xlabel('Features')
plt.ylabel('Average value')
legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")

plt.show()

features_of_interest2 = ['positive_ratings','negative_ratings']
cluster_summary_filtered2 = cluster_summary[features_of_interest2]

cluster_summary_filtered_T2 = cluster_summary_filtered2.T

cluster_summary_filtered_T2.plot(kind='bar')

plt.xlabel('Features')
plt.ylabel('Average value')
legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")

plt.show()

features_of_interest3 = ['price']
cluster_summary_filtered3 = cluster_summary[features_of_interest3]

cluster_summary_filtered_T3 = cluster_summary_filtered3.T

cluster_summary_filtered_T3.plot(kind='bar')

plt.xlabel('Features')
plt.ylabel('Average value')

legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")

plt.show()

features_of_interest4 = ['positive_ratings']
cluster_summary_filtered4 = cluster_summary[features_of_interest4]

cluster_summary_filtered_T4 = cluster_summary_filtered4.T

cluster_summary_filtered_T4.plot(kind='bar')

plt.xlabel('Features')
plt.ylabel('Average value')
legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")
plt.show()

cluster_summary_filtered6 = cluster_summary.iloc[:,10:34]

cluster_summary_filtered_T6 = cluster_summary_filtered6.T

cluster_summary_filtered_T6.plot(kind='bar')

plt.xlabel('Features')
plt.ylabel('Average value')
legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")

cluster_summary_filtered7 = cluster_summary.iloc[:,35:57]

cluster_summary_filtered_T7 = cluster_summary_filtered7.T

cluster_summary_filtered_T7.plot(kind='bar')

# Add labels for the x and y axes
plt.xlabel('Features')
plt.ylabel('Average value')
legend_labels = ['Obscure Game', 'Popular Game', 'Niche Game']
plt.legend(legend_labels, title="Game Type")

plt.show()