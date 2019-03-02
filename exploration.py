import pandas as pd

data = pd.read_csv("CRDC2013_14.csv", encoding="Latin-1")

print(data["JJ"].value_counts())

print(data["SCH_STATUS_MAGNET"].value_counts())