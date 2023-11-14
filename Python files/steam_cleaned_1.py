
import pandas as pd
df = pd.read_csv('~/Downloads/steam.csv')

def range_to_avg(range_val):
    range_vals = range_val.split('-')
    return str((int(range_vals[0]) + int(range_vals[1])) / 2)
df['owners'] = df['owners'].apply(range_to_avg)
df['owners'] = pd.to_numeric(df['owners'], errors='coerce')
