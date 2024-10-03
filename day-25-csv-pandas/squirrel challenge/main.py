import pandas as pd

sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# counts_by_color = (sq_data.groupby('Primary Fur Color').count())
# print(counts_by_color)
# print(type(counts_by_color))
# print(sq_data['Primary Fur Color'])

counts_by_color = (sq_data['Primary Fur Color'].value_counts())

counts_by_color.to_csv("squirrels_counts_color.csv")
