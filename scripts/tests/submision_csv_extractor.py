import pandas as pd

df = pd.read_csv("data/raw/sample_submission.csv")

print(df.columns.tolist())
print(df.head())