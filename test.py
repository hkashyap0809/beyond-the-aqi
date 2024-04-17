import pandas as pd

df = pd.read_csv("air_quality_data.csv")
unique_values = df['City'].unique()
print(unique_values)